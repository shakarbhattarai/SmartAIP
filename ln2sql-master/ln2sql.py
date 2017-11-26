#!/usr/bin/python
# -*- coding: utf-8 -*

import os, sys, getopt
import unicodedata

from Database import Database
from LangConfig import LangConfig
from Parser import Parser
from Thesaurus import Thesaurus
from StopwordFilter import StopwordFilter
import re
reload(sys)
sys.setdefaultencoding("utf-8")

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def procTrig(checkFlagTrigStmt):
  if "(flag or trigger)" in checkFlagTrigStmt or "(flag or trig)" in checkFlagTrigStmt:
      if "(flag or trig)" in checkFlagTrigStmt:
        checkFlagTrigStmt = checkFlagTrigStmt.replace("(flag or trig)", "(flagortrig)")
      if "(flag or trigger)" in checkFlagTrigStmt:
        checkFlagTrigStmt = checkFlagTrigStmt.replace("(flag or trigger)", "(flagortrig)")
      if "(flagortrigger)" in checkFlagTrigStmt:
        checkFlagTrigStmt = checkFlagTrigStmt.replace("(flagortrigger)", "(flagortrig)")
      checkFlagTrigStmtList = checkFlagTrigStmt.split()
      next_word = checkFlagTrigStmtList[checkFlagTrigStmtList.index("(flagortrig)") + 1]
      prev_word = checkFlagTrigStmtList[checkFlagTrigStmtList.index("(flagortrig)") - 1]
      if(next_word.upper() == "MODIFIER" and prev_word.lower() == "in"):
          prev_words= checkFlagTrigStmtList[:checkFlagTrigStmtList.index("in")]
          next_words = checkFlagTrigStmtList[checkFlagTrigStmtList.index("MODIFIER")+1:]
          return (" ".join(prev_words)+ " in (flag M1,flag M2,flag M3,trigger M1,trigger M2,trigger M3)"+" ".join(next_words))
  else:
      return (checkFlagTrigStmt)


def CreateRequiredString(input_sentence):
    """Remove UNB edit AND flag proc IN (92551, 96110) AND ((TRG.PROC between '99381' and '99385')"""
    input_sentence=procTrig(input_sentence)
    input_sentence=input_sentence.replace('=>','is greater than')
    input_sentence=input_sentence.replace('<','is less than')




    result = re.search('Remove (.*) edit', input_sentence)

    if result is not None:
        for flgValues in result.groups():
            input_sentence=re.sub('Remove (.*) edit','Remove editflg in ('+flgValues+')',input_sentence)
    if input_sentence.__contains__('same'):
        input_sentence=input_sentence.replace('same','same is')
        result=re.search("EXISTS (.*)\)", input_sentence)
        if result is not None:
            a=result.groups(1)[0].split('same is')[1]
            input_sentence=input_sentence.replace(a,GetSubQuery('prv-pt-DOS'))
    return input_sentence




def GetSubQuery(field):

    vars=field.split('-')
    dict={'prv':'prvseq','pt':'patseq','DOS':'dos'}

    query = "SELECT 1 FROM hcilin hlin where 1=1 "
    for each_var in vars:
        toadd=" lin."+dict[each_var.strip()]+" = hlin."+dict[each_var.strip()]
        query=query+toadd
    return query



def afterReplacement(input_sentence):
    return input_sentence.replace('FLAG','').replace('TRIGGER','')

def GetReplacedQuery(query, colName, queryLiteral):


    queryLiteral = queryLiteral.replace('.', ' .')
    spaceToDotWordList = queryLiteral.split()
    indexOfDot = [dot for dot, wrdlst in enumerate(spaceToDotWordList) if '.' in wrdlst]
    wordList = '.'.join(spaceToDotWordList).split('.')
    wordList = list(filter(None, wordList))
    c = 0
    innerC = 0
    for word in colName:
        if word in wordList:
            index = [i for i, x in enumerate(wordList) if x == word]
            if query[c] == 'FLAG':

                wordList[index[innerC] - 1] = 'lin'
                innerC += 1
            if query[c] == 'TRIGGER':
                wordList[index[innerC] - 1] = 'trig'
                innerC += 1
            c = c + 1
    for val in indexOfDot:
        wordList[val] = '.' + wordList[val]
    updatedQuery = ' '.join(wordList)
    return updatedQuery.replace(' .', '.')



class ln2sql:
    def __init__(self, database_path, language_path, input_sentence, json_output_path, thesaurus_path, stopwords_path):

        database = Database()
        stopwordsFilter = None

        if thesaurus_path is not None:
            thesaurus = Thesaurus()
            thesaurus.load(thesaurus_path)
            database.set_thesaurus(thesaurus)

        if stopwords_path is not None:
            stopwordsFilter = StopwordFilter()
            stopwordsFilter.load(stopwords_path)
        
        database.load(database_path)
        #database.print_me()

        config = LangConfig()
        config.load(language_path)

        parser = Parser(database, config)


        input_sentence=CreateRequiredString(input_sentence)

        parser.parse_sentence(input_sentence, stopwordsFilter)

        a, b = parser.get_prefix_values()
        print a, b


        #
        # for col in a:
        #
        #     if input_sentence.strip().__contains__('= ('+col):
        #         a= re.search(('.* in \(' + col + '.*\)'), input_sentence.strip()())
        #         print a.groups()
        #         print "sdfdsfds"

        input_sentence=afterReplacement(input_sentence)

        queries = parser.parse_sentence(input_sentence, stopwordsFilter)

        if json_output_path is not None:
            self.remove_json(json_output_path)
            for query in queries:
                query.print_json(json_output_path)

        for query in queries:

            print GetReplacedQuery(b, a, query.__str__())




    def remove_json(self, filename="output.json"):
        if os.path.exists(filename):
            os.remove(filename)

def print_help_message():
    print '\n'
    print 'Usage:'
    print '\tpython ln2sql.py -d <path> -l <path> -i <input-sentence> [-j <path>] [-t <path>] [-s <path>]'
    print 'Parameters:'
    print '\t-h\t\t\tprint this help message'
    print '\t-d <path>\t\tpath to SQL dump file'
    print '\t-l <path>\t\tpath to language configuration file'
    print '\t-i <input-sentence>\tinput sentence to parse'
    print '\t-j <path>\t\tpath to JSON output file'
    print '\t-t <path>\t\tpath to thesaurus file'
    print '\t-s <path>\t\tpath to stopwords file'
    print '\n'




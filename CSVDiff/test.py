
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
          print (" ".join(prev_words)+ " in (flag M1,flag M2,flag M3,trigger M1,trigger M2,trigger M3)"+" ".join(next_words))
  else:
      print (checkFlagTrigStmt)

desc="""Remove ("CPD", DUP) edit 
AND FLAG proc = 'T1015'
AND '25' in (flag or trigger) MODIFIER
AND (SUM of proc 'T1015' 
      AND ( ADJSTATUS 'O’, 'C') AND (ADJPAID >$0)
      AND same PT
      AND same DOS
      <=3)"""
#checkFlagTrigStmt="'25' in (flag, trig) MODIFIER"
procTrig(desc)








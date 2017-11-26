import wordninja
member=['MEM','MEMBER']
placeofservice=["PLACEOFSERVICE"]
service =["SERVICE"]
dob = ['PATIENT_DOB',
                'PERSON_DOB',
                'DOB',
                'PATDOB',
                'MBR_DOB_DT',
                'EMPDOB',
                'SAS_PATIENT_DOB',
                'MEM_DOB',
                'MBRDOB',
                'MEDMEMBERDOB',
                'CLAINANTPATIENTDOB',
                'PATIENTDOB',
                'PAT_DOB',
                'MBRDOB',
                'CLAIMANT_DOB',
                'MEMDOBCC',
                'MEMBERSDOB',
                'PERSON_DOB',
                'MEMBER_DOB',
                'DOB',
                'MBR_DOB',
                'MBR_DOB_DT',
                'CLAIMANTDOB',
                'SUBSCRIBERS_DOB',
                'DEPDOB',
                'PATN_DOB',
                'EMPLOYEE_DOB',
                'PATIENTDOB',
                'MEMBER_DOB_DATE',
                'PTDOB',
                'MEMBERDOB',
                'MEMBERDOB',
                'CLAIMANT_DOB',
                'DOB_DT',
                'MEDMEMBERDOB',
                'PATIENTDOB',
                'PATDOB',
                'MEM_DOB',
                'CLMNT_DOB',
                'DEPDOB',
                'PATIENT_DOB',
                'MEMDOB',
                'EMPDOB',
                'MEMBER_DOB',
                'EE_DOB',
                'MDOB',
                'FULL_PAT_DOB',
                'DOB',
                'PATDOB',
                'PAT_DOB',
                'MEMBER_DOB',
                'CLMH_PDOB',
                'MEMBERSDOB',
                'PDOB',
                'PAT_DOB_DT',
                'MEDMEMBERDOB',
                'BRTH_DT']

def rule(inputWord):
    if inputWord in dob:
        return "DOB"
    if inputWord in member:
        return "MEMBER"
    if inputWord in placeofservice:
        return "PLACEOFSERVICE"
    if inputWord in service:
        return "SERVICE"
    return ""

def checkForRule(doc1, doc2):
    match1=""
    match2=""
    for word in doc1:
        match1+= rule(word)
    for word in doc2:
        match2 += rule(word)
    print(match1, match2)
    if match1 and match2 and match1 == match2:
        return True
    else:
        return False

field1="fname"
field2="first_name"
doc1= wordninja.split(field1.lower())
doc2= wordninja.split(field2.lower())
print(doc1,doc2)
print(checkForRule(doc1,doc2))
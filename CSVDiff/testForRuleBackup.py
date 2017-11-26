import itertools
import wordninja

from CSVDiff import rxClaim

def rule(inputWord):
    if inputWord in rxClaim.total:
        return "total"
    if inputWord in rxClaim.sales:
        return "sales"
    if inputWord in rxClaim.tax:
        return "tax"
    if inputWord in rxClaim.percentage:
        return "percentage"
    if inputWord in rxClaim.day:
        return "day"
    if inputWord in rxClaim.supply:
        return "daysupply"
    if inputWord in rxClaim.per:
        return "per"
    if inputWord in rxClaim.ucf:
        return "ucf"
    if inputWord in rxClaim.dispensing:
        return "dispensing"
    if inputWord in rxClaim.ingredient:
        return "ingredient"
    if inputWord in rxClaim.submit:
        return "submit"
    if inputWord in rxClaim.subgroup:
        return "subgroup"
    if inputWord in rxClaim.plan:
        return "plan"
    if inputWord in rxClaim.billed:
        return "billed"
    if inputWord in rxClaim.approved:
        return "approved"
    if inputWord in rxClaim.number:
        return "number"
    if inputWord in rxClaim.allowed:
        return "allowed"
    if inputWord in rxClaim.fee:
        return "fee"
    if inputWord in rxClaim.code:
        return "code"
    if inputWord in rxClaim.ndc:
        return "ndc"
    if inputWord in rxClaim.prescriber:
        return "prescriber"
    if inputWord in rxClaim.firstname:
        return "firstname"
    if inputWord in rxClaim.lastname:
        return "lastname"
    if inputWord in rxClaim.qualifer:
        return "qualifer"
    if inputWord in rxClaim.patient:
        return "patient"
    if inputWord in rxClaim.gender:
        return "gender"
    if inputWord in rxClaim.member:
        return "member"
    if inputWord in rxClaim.pharmacy:
        return "pharmacy"
    if inputWord in rxClaim.type:
        return "type"
    if inputWord in rxClaim.indicator:
        return "indicator"
    if inputWord in rxClaim.drug:
        return "drug"
    if inputWord in rxClaim.amount:
        return "amount"
    if inputWord in rxClaim.paid:
        return "paid"
    if inputWord in rxClaim.pay:
        return "pay"
    if inputWord in rxClaim.date:
        return "date"
    if inputWord in rxClaim.record:
        return "record"
    if inputWord in rxClaim.person:
        return "person"
    if inputWord in rxClaim.drugstrength:
        return "drugstrength"
    if inputWord in rxClaim.cost:
        return "cost"
    if inputWord in rxClaim.batch:
        return "batch"
    if inputWord in rxClaim.unit:
        return "unit"
    if inputWord in rxClaim.quantity:
        return "quantity"
    if inputWord in rxClaim.metric:
        return "metric"
    if inputWord in rxClaim.dob:
        return "dob"
    if inputWord in rxClaim.birth:
        return "birth"
    if inputWord in rxClaim.identifier:
        return "identifier"
    if inputWord in rxClaim.other:
        return "other"
    if inputWord in rxClaim.coverage:
        return "coverage"
    if inputWord in rxClaim.compound:
        return "compound"
    if inputWord in rxClaim.ssn:
        return "ssn"
    if inputWord in rxClaim.fill:
        return "fill"
    if inputWord in rxClaim.time:
        return "time"
    if inputWord in rxClaim.awp:
        return "awp"
    if inputWord in rxClaim.city:
        return "city"
    if inputWord in rxClaim.state:
        return "state"
    if inputWord in rxClaim.status:
        return "status"
    if inputWord in rxClaim.name:
        return "name"
    if inputWord in rxClaim.group:
        return "group"
    if inputWord in rxClaim.copay:
        return "copay"
    if inputWord in rxClaim.rx:
        return "rx"
    if inputWord in rxClaim.zip:
        return "zip"
    if inputWord in rxClaim.id:
        return "id"
    if inputWord in rxClaim.relationship:
        return "relationship"
    if inputWord in rxClaim.level:
        return "level"
    if inputWord in rxClaim.claims:
        return "claims"
    if inputWord in rxClaim.origin:
        return "origin"
    if inputWord in rxClaim.service:
        return "service"
    if inputWord in rxClaim.coinsurance:
        return "coinsurance"
    if inputWord in rxClaim.refill:
        return "refill"
    if inputWord in rxClaim.authorized:
        return "authorized"
    if inputWord in rxClaim.eligibility:
        return "eligibility"
    if inputWord in rxClaim.ineligible:
        return "ineligible"
    if inputWord in rxClaim.clarification:
        return "clarification"
    if inputWord in rxClaim.reason:
        return "reason"
    if inputWord in rxClaim.card:
        return "card"
    if inputWord in rxClaim.holder:
        return "holder"
    if inputWord in rxClaim.deduct:
        return "deduct"
    if inputWord in rxClaim.processor:
        return "processor"
    if inputWord in rxClaim.flag:
        return "flag"
    if inputWord in rxClaim.filter:
        return "filter"
    if inputWord in rxClaim.formulary:
        return "formulary"
    if inputWord in rxClaim.new:
        return "new"
    if inputWord in rxClaim.moi:
        return "moi"
    if inputWord in rxClaim.order:
        return "order"
    if inputWord in rxClaim.mail:
        return "mail"
    if inputWord in rxClaim.nonmail:
        return "nonmail"
    if inputWord in rxClaim.diagnosis:
        return "diagnosis"
    if inputWord in rxClaim.cob:
        return "cob"
    if inputWord in rxClaim.benefit:
        return "benefit"
    if inputWord in rxClaim.dose:
        return "dose"
    if inputWord in rxClaim.basis:
        return "basis"
    if inputWord in rxClaim.determination:
        return "determination"
    if inputWord in rxClaim.daw:
        return "daw"
    if inputWord in rxClaim.written:
        return "written"
    if inputWord in rxClaim.adjudication:
        return "adjudication"
    if inputWord in rxClaim.age:
        return "age"
    if inputWord in rxClaim.adjustment:
        return "adjustment"
    if inputWord in rxClaim.product:
        return "product"
    if inputWord in rxClaim.expansion:
        return "expansion"
    if inputWord in rxClaim.area:
        return "area"
    if inputWord in rxClaim.area1:
        return "area1"
    if inputWord in rxClaim.area2:
        return "area2"
    if inputWord in rxClaim.transaction:
        return "transaction"
    if inputWord in rxClaim.source:
        return "source"
    if inputWord in rxClaim.enr:
        return "enr"
    if inputWord in rxClaim.admin:
        return "admin"
    if inputWord in rxClaim.count:
        return "count"
    if inputWord in rxClaim.primary:
        return "primary"
    if inputWord in rxClaim.sequence:
        return "sequence"
    if inputWord in rxClaim.generic:
        return "generic"
    if inputWord in rxClaim.label:
        return "label"
    if inputWord in rxClaim.home:
        return "home"
    if inputWord in rxClaim.phone:
        return "phone"
    if inputWord in rxClaim.provider:
        return "provider"
    if inputWord in rxClaim.account:
        return "account"
    if inputWord in rxClaim.measure:
        return "measure"
    if inputWord in rxClaim.discount:
        return "discount"
    if inputWord in rxClaim.metric:
        return "metric"
    if inputWord in rxClaim.work:
        return "work"
    if inputWord in rxClaim.npi:
        return "npi"
    if inputWord in rxClaim.national:
        return "national"
    if inputWord in rxClaim.carrier:
        return "carrier"
    if inputWord in rxClaim.maintenance:
        return "maintenance"
    if inputWord in rxClaim.injury:
        return "injury"
    if inputWord in rxClaim.check:
        return "check"
    if inputWord in rxClaim.description:
        return "description"
    if inputWord in rxClaim.customer:
        return "customer"
    if inputWord in rxClaim.location:
        return "location"
    if inputWord in rxClaim.category:
        return "category"
    if inputWord in rxClaim.reject:
        return "reject"
    if inputWord in rxClaim.tier:
        return "tier"
    if inputWord in rxClaim.residence:
        return "residence"
    if inputWord in rxClaim.facility:
        return "facility"
    if inputWord in rxClaim.pos:
        return "pos"
    if inputWord in rxClaim.place:
        return "place"
    if inputWord in rxClaim.package:
        return "package"
    if inputWord in rxClaim.route:
        return "route"
    if inputWord in rxClaim.sic:
        return "sic"
    if inputWord in rxClaim.host:
        return "host"
    if inputWord in rxClaim.net:
        return "net"
    if inputWord in rxClaim.gcn:
        return "gcn"
    if inputWord in rxClaim.gross:
        return "gross"
    if inputWord in rxClaim.due:
        return "due"
    if inputWord in rxClaim.brand:
        return "brand"
    if inputWord in rxClaim.modifier:
        return "modifier"
    if inputWord in rxClaim.level1:
        return "level1"
    if inputWord in rxClaim.level2:
        return "level2"
    if inputWord in rxClaim.level3:
        return "level3"
    if inputWord in rxClaim.level1description:
        return "level1description"
    if inputWord in rxClaim.level2description:
        return "level2description"
    if inputWord in rxClaim.level3description:
        return "level3description"
    if inputWord in rxClaim.line:
        return "line"
    if inputWord in rxClaim.nabp:
        return "nabp"
    if inputWord in rxClaim.middle:
        return "middle"
    if inputWord in rxClaim.initial:
        return "initial"
    if inputWord in rxClaim.hmo:
        return "hmo"
    if inputWord in rxClaim.classlist:
        return "classlist"
    if inputWord in rxClaim.thrptc:
        return "thrptc"
    if inputWord in rxClaim.thrpdc:
        return "thrpdc"
    if inputWord in rxClaim.alternate:
        return "alternate"
    if inputWord in rxClaim.nt:
        return "nt"
    if inputWord in rxClaim.dean:
        return "dean"
    if inputWord in rxClaim.strength:
        return "strength"



    # if inputWord in claimRule.placeofservice:
    #     return "PLACEOFSERVICE"
    # if inputWord in claimRule.service:
    #     return "SERVICE"
    #if inputWord in
    return ""

def checkForRule(doc1, doc2):
    match1=[]
    match2=[]
    for word in doc1:
        match1.append(rule(word))
    for word in doc2:
        match2.append(rule(word))
    match1 = list(filter(None, match1))
    match2 = list(filter(None, match2))
    print(match1, match2)
    if match1 and match2 and (set(match1) == set(match2) or "".join(set(match1)) == "".join(set(match2))):
        return True
    else:
        if(len(match1) > 1):
            match1List = list(itertools.permutations(match1))
        else:
            match1List = match1
        if(len(match2) > 1):
            match2List = list((itertools.permutations(match2)))
        else:
            match2List = match2
        for permutation1 in match1List:
            for permutation2 in match2List:
                if match1List and match2List and rule("".join(permutation1)) == rule("".join(permutation2)):
                    print(permutation1, permutation2)
                    return True
        print(match1List,match2List)
        return False

field1="days_supply"
field2="supply"
doc1= wordninja.split(field1.lower())
doc2= wordninja.split(field2.lower())
print(doc1,doc2)
print(checkForRule(doc1,doc2))
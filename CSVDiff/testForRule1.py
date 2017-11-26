import itertools
import wordninja

from CSVDiff import rxClaim
from CSVDiff import diagClaim
from CSVDiff import elig

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
        return "supply"
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
    if inputWord in rxClaim.first:
        return "first"
    if inputWord in rxClaim.last:
        return "last"
    if inputWord in rxClaim.manufacture:
        return "manufacture"
    if inputWord in rxClaim.unc:
        return "unc"
    if inputWord in rxClaim.out:
        return "out"
    if inputWord in rxClaim.pocket:
        return "pocket"
    if inputWord in rxClaim.apply:
        return "apply"
    if inputWord in rxClaim.preauth:
        return "preauth"
    if inputWord in rxClaim.sfx:
        return "sfx"
    if inputWord in rxClaim.mac:
        return "mac"
    if inputWord in rxClaim.price:
        return "price"
    if inputWord in rxClaim.therapeutic:
        return "therapeutic"
    if inputWord in rxClaim.chapter:
        return "chapter"
    if inputWord in rxClaim.special:
        return "special"
    if inputWord in rxClaim.client:
        return "client"
    if inputWord in rxClaim.ahfs:
        return "ahfs"
    if inputWord in rxClaim.run:
        return "run"
    if inputWord in rxClaim.department:
        return "department"
    if inputWord in rxClaim.insurance:
        return "insurance"
    if inputWord in rxClaim.incentive:
        return "incentive"
    if inputWord in rxClaim.reduced:
        return "reduced"
    if inputWord in rxClaim.usual:
        return "usual"
    if inputWord in rxClaim.charge:
        return "charge"
    if inputWord in rxClaim.intended:
        return "intended"
    if inputWord in rxClaim.sub:
        return "sub"
    if inputWord in rxClaim.segment:
        return "segment"
    if inputWord in rxClaim.calculation:
        return "calculation"
    if inputWord in rxClaim.brance:
        return "brance"
    if inputWord in rxClaim.invoice:
        return "invoice"
    if inputWord in rxClaim.attribute:
        return "attribute"
    if inputWord in rxClaim.flat:
        return "flat"
    if inputWord in rxClaim.contract:
        return "contract"
    if inputWord in rxClaim.physn:
        return "physn"
    if inputWord in rxClaim.address:
        return "address"
    if inputWord in rxClaim.fullawp:
        return "fullawp"
    if inputWord in rxClaim.database:
        return "database"
    if inputWord in rxClaim.media:
        return "media"
    if inputWord in rxClaim.sn:
        return "sn"
    if inputWord in rxClaim.subscriber:
        return "subscriber"
    if inputWord in rxClaim.designator:
        return "designator"
    if inputWord in rxClaim.script:
        return "script"
    if inputWord in rxClaim.receiver:
        return "receiver"
    if inputWord in rxClaim.post:
        return "post"
    if inputWord in rxClaim.master:
        return "master"
    if inputWord in rxClaim.gpi:
        return "gpi"
    if inputWord in rxClaim.original:
        return "original"
    if inputWord in rxClaim.mcdr:
        return "mcdr"
    if inputWord in rxClaim.vendor:
        return "vendor"
    if inputWord in rxClaim.batch:
        return "batch"
    if inputWord in rxClaim.file:
        return "file"
    if inputWord in rxClaim.resubmission:
        return "resubmission"
    if inputWord in rxClaim.cycle:
        return "cycle"
    if inputWord in rxClaim.reference:
        return "reference"
    if inputWord in rxClaim.professional:
        return "professional"
    if inputWord in rxClaim.care:
        return "care"
    if inputWord in rxClaim.remaining:
        return "remaining"
    if inputWord in rxClaim.hold:
        return "hold"
    if inputWord in rxClaim.harmless:
        return "harmless"
    if inputWord in rxClaim.preferred:
        return "preferred"
    if inputWord in rxClaim.prior:
        return "prior"
    if inputWord in rxClaim.innetwork:
        return "innetwork"
    if inputWord in rxClaim.excess:
        return "excess"
    if inputWord in rxClaim.override:
        return "override"
    if inputWord in rxClaim.medicare:
        return "medicare"
    if inputWord in rxClaim.recovery:
        return "recovery"
    if inputWord in rxClaim.version:
        return "version"
    if inputWord in rxClaim.release:
        return "release"
    if inputWord in rxClaim.recognized:
        return "recognized"
    if inputWord in rxClaim.average:
        return "average"
    if inputWord in rxClaim.federal:
        return "federal"
    if inputWord in rxClaim.memo:
        return "memo"
    if inputWord in rxClaim.end:
        return "end"
    if inputWord in rxClaim.upper:
        return "upper"
    if inputWord in rxClaim.limit:
        return "limit"
    if inputWord in rxClaim.land:
        return "land"
    if inputWord in rxClaim.fda:
        return "fda"
    if inputWord in rxClaim.efficacy:
        return "efficacy"
    if inputWord in rxClaim.policy:
        return "policy"
    if inputWord in rxClaim.network:
        return "network"
    if inputWord in rxClaim.reimbursement:
        return "reimbursement"
    if inputWord in rxClaim.cut:
        return "cut"
    if inputWord in rxClaim.back:
        return "back"
    if inputWord in rxClaim.medical:
        return "medical"
    if inputWord in rxClaim.value:
        return "value"
    if inputWord in rxClaim.cross:
        return "cross"
    if inputWord in rxClaim.nott:
        return "nott"
    if inputWord in rxClaim.user:
        return "user"
    if inputWord in rxClaim.result:
        return "result"
    if inputWord in rxClaim.accumulated:
        return "accumulated"
    if inputWord in rxClaim.difference:
        return "difference"
    if inputWord in rxClaim.dependent:
        return "dependent"
    if inputWord in rxClaim.ee:
        return "ee"
    if inputWord in rxClaim.severity1:
        return "severity1"
    if inputWord in rxClaim.severity2:
        return "severity2"
    if inputWord in rxClaim.message2:
        return "message2"
    if inputWord in rxClaim.message3:
        return "message3"
    if inputWord in rxClaim.message1:
        return "message1"
    if inputWord in rxClaim.fsa:
        return "fsa"
    if inputWord in rxClaim.creation:
        return "creation"
    if inputWord in rxClaim.auth:
        return "auth"
    if inputWord in rxClaim.pica:
        return "pica"
    if inputWord in rxClaim.vaccine:
        return "vaccine"
    if inputWord in rxClaim.waiver:
        return "waiver"
    if inputWord in rxClaim.defined:
        return "defined"
    if inputWord in rxClaim.data:
        return "data"
    if inputWord in rxClaim.insulin:
        return "insulin"
    if inputWord in rxClaim.month:
        return "month"
    if inputWord in rxClaim.proc:
        return "proc"
    if inputWord in rxClaim.report:
        return "report"
    if inputWord in rxClaim.pamcsc:
        return "pamcsc"
    if inputWord in rxClaim.cltslstax:
        return "cltslstax"
    if inputWord in rxClaim.cltatrded:
        return "cltatrded"
    if inputWord in rxClaim.postal:
        return "postal"
    if inputWord in rxClaim.select:
        return "select"
    if inputWord in rxClaim.non:
        return "non"
    if inputWord in rxClaim.period:
        return "period"
    if inputWord in rxClaim.cltingrcst:
        return "cltingrcst"
    if inputWord in rxClaim.payor:
        return "payor"
    if inputWord in rxClaim.pbp:
        return "payor"
    if inputWord in rxClaim.sending:
        return "sending"
    if inputWord in rxClaim.entity:
        return "entity"
    if inputWord in rxClaim.socsecnbr:
        return "socsecnbr"
    if inputWord in rxClaim.decimal:
        return "decimal"

    return claimRule(inputWord)



    # if inputWord in claimRule.placeofservice:
    #     return "PLACEOFSERVICE"
    # if inputWord in claimRule.service:
    #     return "SERVICE"
    #if inputWord in
    #return ""

def claimRule(inputWord):
    if inputWord in diagClaim.claim:
        return "claim"
    if inputWord in diagClaim.procedure:
        return "procedure"
    if inputWord in diagClaim.member:
        return "member"
    if inputWord in diagClaim.code:
        return "code"
    if inputWord in diagClaim.gender:
        return "gender"
    if inputWord in diagClaim.paid:
        return "paid"
    if inputWord in diagClaim.payment:
        return "payment"
    if inputWord in diagClaim.date:
        return "date"
    if inputWord in diagClaim.number:
        return "number"
    if inputWord in diagClaim.dob:
        return "dob"
    if inputWord in diagClaim.claimant:
        return "claimant"
    if inputWord in diagClaim.revenue:
        return "revenue"
    if inputWord in diagClaim.amount:
        return "amount"
    if inputWord in diagClaim.drug:
        return "drug"
    if inputWord in diagClaim.copay:
        return "copay"
    if inputWord in diagClaim.line:
        return "line"
    if inputWord in diagClaim.fromlist:
        return "fromlist"
    if inputWord in diagClaim.typelist:
        return "typelist"
    if inputWord in diagClaim.coinsurance:
        return "coinsurance"
    if inputWord in diagClaim.insurance:
        return "insurance"
    if inputWord in diagClaim.deductible:
        return "deductible"
    if inputWord in diagClaim.units:
        return "units"
    if inputWord in diagClaim.allowed:
        return "allowed"
    if inputWord in diagClaim.provider:
        return "provider"
    if inputWord in diagClaim.modifier:
        return "modifier"
    if inputWord in diagClaim.name:
        return "name"
    if inputWord in diagClaim.bill:
        return "bill"
    if inputWord in diagClaim.service:
        return "service"
    if inputWord in diagClaim.record:
        return "record"
    if inputWord in diagClaim.ssn:
        return "ssn"
    if inputWord in diagClaim.group:
        return "group"
    if inputWord in diagClaim.zip:
        return "zip"
    if inputWord in diagClaim.discharge:
        return "discharge"
    if inputWord in diagClaim.placeofservice:
        return "placeofservice"
    if inputWord in diagClaim.city:
        return "city"
    if inputWord in diagClaim.adjustment:
        return "adjustment"
    if inputWord in diagClaim.patient:
        return "patient"
    if inputWord in diagClaim.first:
        return "first"
    if inputWord in diagClaim.firstname:
        return "firstName"
    if inputWord in diagClaim.lastname:
        return "lastName"
    if inputWord in diagClaim.fullname:
        return "fullname"
    if inputWord in diagClaim.employer:
        return "employer"
    if inputWord in diagClaim.client:
        return "client"
    if inputWord in diagClaim.employee:
        return "employee"
    if inputWord in diagClaim.customer:
        return "customer"
    if inputWord in diagClaim.subscriber:
        return "subscriber"
    if inputWord in diagClaim.flag:
        return "flag"
    if inputWord in diagClaim.relation:
        return "relation"
    if inputWord in diagClaim.desc:
        return "desc"
    if inputWord in diagClaim.count:
        return "count"
    if inputWord in diagClaim.innwk:
        return "innwk"
    if inputWord in diagClaim.nwk:
        return "nwk"
    if inputWord in diagClaim.receive:
        return "receive"
    if inputWord in diagClaim.speciality:
        return "speciality"
    if inputWord in diagClaim.status:
        return "status"
    if inputWord in diagClaim.address:
        return "address"
    if inputWord in diagClaim.enrollee:
        return "enrollee"
    if inputWord in diagClaim.enrollment:
        return "enrollment"
    if inputWord in diagClaim.diagnosis:
        return "diagnosis"
    if inputWord in diagClaim.state:
        return "state"
    if inputWord in diagClaim.cob:
        return "cob"
    if inputWord in diagClaim.coverage:
        return "coverage"
    if inputWord in diagClaim.save:
        return "save"
    if inputWord in diagClaim.source:
        return "source"
    if inputWord in diagClaim.cptii:
        return "cptii"
    if inputWord in diagClaim.work:
        return "work"
    if inputWord in diagClaim.savings:
        return "savings"
    if inputWord in diagClaim.typeofservice:
        return "typeofservice"
    if inputWord in diagClaim.through:
        return "through"
    if inputWord in diagClaim.day:
        return "day"
    if inputWord in diagClaim.category:
        return "category"
    if inputWord in diagClaim.package:
        return "package"
    if inputWord in diagClaim.quantity:
        return "quantity"
    if inputWord in diagClaim.charge:
        return "charge"
    if inputWord in diagClaim.tax:
        return "tax"
    if inputWord in diagClaim.product:
        return "product"
    if inputWord in diagClaim.identifier:
        return "identifier"
    if inputWord in diagClaim.admission:
        return "admission"
    if inputWord in diagClaim.location:
        return "location"
    if inputWord in diagClaim.level:
        return "level"
    if inputWord in diagClaim.lab:
        return "lab"
    if inputWord in diagClaim.test:
        return "test"
    if inputWord in diagClaim.plan:
        return "plan"
    if inputWord in diagClaim.check:
        return "check"
    if inputWord in diagClaim.indicator:
        return "indicator"
    if inputWord in diagClaim.start:
        return "start"
    if inputWord in diagClaim.cur:
        return "cur"
    if inputWord in diagClaim.occurance:
        return "occurance"
    if inputWord in diagClaim.incurred:
        return "incurred"
    if inputWord in diagClaim.sequence:
        return "sequence"
    if inputWord in diagClaim.branch:
        return "branch"
    if inputWord in diagClaim.contract:
        return "contract"
    if inputWord in diagClaim.account:
        return "account"
    if inputWord in diagClaim.major:
        return "major"
    if inputWord in diagClaim.mdc:
        return "mdc"
    if inputWord in diagClaim.benefit:
        return "benefit"
    if inputWord in diagClaim.benefitdiscountamount:
        return "benefitDiscountAmount"
    if inputWord in diagClaim.capitation:
        return "capitation"
    if inputWord in diagClaim.person:
        return "person"
    if inputWord in diagClaim.covered:
        return "covered"
    if inputWord in diagClaim.primary:
        return "primary"
    if inputWord in diagClaim.empgncrcd:
        return "empgncrcd"
    if inputWord in diagClaim.dependent:
        return "dependent"
    if inputWord in diagClaim.transaction:
        return "transaction"
    if inputWord in diagClaim.transfer:
        return "transfer"
    if inputWord in diagClaim.segment:
        return "segment"
    if inputWord in diagClaim.discount:
        return "discount"
    if inputWord in diagClaim.proddistnctncd:
        return "proddistnctncd"
    if inputWord in diagClaim.capacity:
        return "capacity"
    if inputWord in diagClaim.aexplandsgntncd:
        return "aexplandsgntncd"
    if inputWord in diagClaim.adjprvdrdsgnncd:
        return "adjprvdrdsgnncd"
    if inputWord in diagClaim.plspprodcd:
        return "plspprodcd"
    if inputWord in diagClaim.ahfbfdamt:
        return "ahfbfdamt"
    if inputWord in diagClaim.elligible:
        return "elligible"
    if inputWord in diagClaim.method:
        return "method"
    if inputWord in diagClaim.reason:
        return "reason"
    if inputWord in diagClaim.reject:
        return "reject"
    if inputWord in diagClaim.encounter:
        return "encounter"
    if inputWord in diagClaim.negotiated:
        return "negotiated"
    if inputWord in diagClaim.version:
        return "version"
    if inputWord in diagClaim.prefer:
        return "prefer"
    if inputWord in diagClaim.business:
        return "business"
    if inputWord in diagClaim.render:
        return "render"
    if inputWord in diagClaim.ppo:
        return "ppo"
    if inputWord in diagClaim.disposition:
        return "disposition"
    if inputWord in diagClaim.dispense:
        return "dispense"
    if inputWord in diagClaim.carrier:
        return "carrier"
    if inputWord in diagClaim.therapeutic:
        return "therapeutic"
    if inputWord in diagClaim.treatment:
        return "treatment"
    if inputWord in diagClaim.policy:
        return "policy"
    if inputWord in diagClaim.filling:
        return "filling"
    if inputWord in diagClaim.formulary:
        return "formulary"
    if inputWord in diagClaim.chain:
        return "chain"
    if inputWord in diagClaim.reporting:
        return "reporting"
    if inputWord in diagClaim.institutional:
        return "institutional"
    if inputWord in diagClaim.differential:
        return "differential"
    if inputWord in diagClaim.ingredient:
        return "ingredient"
    if inputWord in diagClaim.receipt:
        return "receipt"
    if inputWord in diagClaim.requirement:
        return "requirement"
    if inputWord in diagClaim.present:
        return "present"
    if inputWord in diagClaim.hospital:
        return "hospital"
    if inputWord in diagClaim.process:
        return "process"
    if inputWord in diagClaim.limit:
        return "limit"
    if inputWord in diagClaim.exclusion:
        return "limit"
    if inputWord in diagClaim.work:
        return "work"
    if inputWord in diagClaim.compensation:
        return "compensation"
    if inputWord in diagClaim.reduce:
        return "reduce"
    if inputWord in diagClaim.region:
        return "region"
    if inputWord in diagClaim.accident:
        return "accident"
    if inputWord in diagClaim.secondary:
        return "secondary"
    if inputWord in diagClaim.referral:
        return "referral"
    if inputWord in diagClaim.liability:
        return "liability"
    if inputWord in diagClaim.agency:
        return "agency"
    if inputWord in diagClaim.original:
        return "original"
    if inputWord in diagClaim.federal:
        return "federal"
    if inputWord in diagClaim.withhold:
        return "withhold"
    if inputWord in diagClaim.payer:
        return "payer"
    if inputWord in diagClaim.pyrllctn:
        return "pyrllctn"
    if inputWord in diagClaim.denial:
        return "denial"
    if inputWord in diagClaim.undisclose:
        return "undisclose"
    if inputWord in diagClaim.revision:
        return "revision"
    if inputWord in diagClaim.agreement:
        return "agreement"
    if inputWord in diagClaim.encounter:
        return "encounter"
    if inputWord in diagClaim.classification:
        return "classification"
    eligRule(inputWord)

def eligRule(inputWord):
    if inputWord in elig.city:
        return "city"
    if inputWord in elig.state:
        return "state"
    if inputWord in elig.gender:
        return "gender"
    if inputWord in elig.record:
        return "record"
    if inputWord in elig.dob:
        return "dob"
    if inputWord in elig.ssn:
        return "ssn"
    if inputWord in elig.zip:
        return "zip"
    if inputWord in elig.first:
        return "first"
    if inputWord in elig.firstName:
        return "firstName"
    if inputWord in elig.lastName:
        return "lastName"
    if inputWord in elig.fullname:
        return "fullname"
    if inputWord in elig.coverage:
        return "coverage"
    if inputWord in elig.member:
        return "member"
    if inputWord in elig.address:
        return "address"
    if inputWord in elig.relation:
        return "relation"
    if inputWord in elig.termination:
        return "termination"
    if inputWord in elig.phone:
        return "phone"
    if inputWord in elig.effective:
        return "effective"
    if inputWord in elig.flag:
        return "flag"
    if inputWord in elig.subscriber:
        return "subscriber"
    if inputWord in elig.enrollee:
        return "enrollee"
    if inputWord in elig.enrollment:
        return "enrollment"
    if inputWord in elig.typelist:
        return "typelist"
    if inputWord in elig.desc:
        return "desc"
    if inputWord in elig.care:
        return "care"
    if inputWord in elig.physician:
        return "physician"
    if inputWord in elig.cms:
        return "cms"
    if inputWord in elig.centers:
        return "centers"
    if inputWord in elig.medicare:
        return "medicare"
    if inputWord in elig.medicaid:
        return "medicaid"
    if inputWord in elig.beneficiary:
        return "beneficiary"
    if inputWord in elig.sic:
        return "sic"
    if inputWord in elig.hire:
        return "hire"
    if inputWord in elig.payer:
        return "payer"
    if inputWord in elig.division:
        return "division"
    if inputWord in elig.medical:
        return "medical"
    if inputWord in elig.suffix:
        return "suffix"
    if inputWord in elig.group:
        return "group"
    if inputWord in elig.number:
        return "number"
    if inputWord in elig.status:
        return "status"
    if inputWord in elig.source:
        return "source"
    if inputWord in elig.plan:
        return "plan"
    if inputWord in elig.date:
        return "date"
    if inputWord in elig.employer:
        return "employer"
    if inputWord in elig.client:
        return "client"
    if inputWord in elig.employee:
        return "employee"
    if inputWord in elig.dependent:
        return "dependent"
    if inputWord in elig.plan:
        return "plan"
    if inputWord in elig.product:
        return "product"
    if inputWord in elig.package:
        return "package"
    if inputWord in elig.units:
        return "units"
    if inputWord in elig.employement:
        return "employement"
    if inputWord in elig.medical:
        return "medical"
    if inputWord in elig.category:
        return "category"
    if inputWord in elig.business:
        return "business"
    if inputWord in elig.transaction:
        return "transaction"
    if inputWord in elig.contract:
        return "contract"
    if inputWord in elig.country:
        return "country"
    if inputWord in elig.initial:
        return "initial"
    if inputWord in elig.location:
        return "location"
    if inputWord in elig.sequence:
        return "sequence"
    if inputWord in elig.eligibility:
        return "eligibility"
    if inputWord in elig.created:
        return "created"
    if inputWord in elig.division:
        return "division"
    if inputWord in elig.alternate:
        return "alternate"
    if inputWord in elig.vision:
        return "vision"
    if inputWord in elig.option:
        return "option"
    if inputWord in elig.carrier:
        return "carrier"
    if inputWord in elig.postal:
        return "postal"
    if inputWord in elig.dental:
        return "dental"
    if inputWord in elig.prescription:
        return "prescription"
    if inputWord in elig.account:
        return "account"
    if inputWord in elig.health:
        return "health"
    if inputWord in elig.benefit:
        return "benefit"
    if inputWord in elig.region:
        return "region"
    if inputWord in elig.receive:
        return "receive"
    if inputWord in elig.lastName:
        return "lastName"
    if inputWord in elig.character:
        return "character"
    if inputWord in elig.mental:
        return "mental"
    if inputWord in elig.original:
        return "original"
    if inputWord in elig.scheduled:
        return "scheduled"
    if inputWord in elig.department:
        return "department"
    if inputWord in elig.identifier:
        return "identifier"
    if inputWord in elig.indicator:
        return "indicator"
    if inputWord in elig.drug:
        return "drug"
    if inputWord in elig.lob:
        return "lob"
    if inputWord in elig.count:
        return "count"
    if inputWord in elig.classification:
        return "classification"
    if inputWord in elig.contribution:
        return "contribution"
    if inputWord in elig.premium:
        return "premium"

    return ""


def checkForRule(doc1, doc2):
    match1=[]
    match2=[]
    for word in doc1:
        match1.append(rule(word))
    for word in doc2:
        match2.append(rule(word))
    if None in match1:
        return False, match1, match2
    if None in match2:
        return False, match1, match2
    match1 = list(filter(None, match1))
    match2 = list(filter(None, match2))
    # print(match1, match2)
    if match1 and match2 and (set(match1) == set(match2) or "".join(set(match1)) == "".join(set(match2))):
        return True, match1, match2
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
                out1=rule("".join(permutation1))
                out2=rule("".join(permutation2))
                if(out1 is not None and out2 is not None ):
                    if match1List and match2List and out1 == out2:
                        #print(permutation1,permutation2)
                        #print("".join(permutation1), "".join(permutation2))
                        return True,match1,match2
        #print(match1List,match2List)
        return False,match1,match2

# field1="statuscode"
# field2="date_paid"
# doc1= wordninja.split(field1.lower())
# doc2= wordninja.split(field2.lower())
# print(doc1,doc2)
# isFoundInRule, standard1, standard2 = checkForRule(doc1,doc2)
# print(isFoundInRule)
# print(standard1)
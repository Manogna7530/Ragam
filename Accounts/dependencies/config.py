from django.conf import settings
import os

fileLoc = settings.MEDIA_ROOT / 'Accounts'
if not os.path.isdir(fileLoc):
    os.mkdir(fileLoc)

homeLoc = fileLoc / 'home'
if not os.path.isdir(homeLoc):
    os.mkdir(homeLoc)

ICONS = {
    'count': 'sop-patient',
    'time': 'sop-time',

    # 'local': '<local>',
    # 'international': '<international>',

    'ultrasound': 'sop-ultrasound',
    'flouroscopy': 'sop-flouroscopy',
    'x-ray section': 'sop-x-ray',
    'mri section': 'sop-mri',
    'mammogram': 'sop-mammography',
    'ct-scan section': 'sop-ct-scan',
    
    'opd': "sop-opd",
    'ip': "sop-inpatient",
    'er': "sop-er",

    'reg': "sop-registration",
    'twt': "sop-triage",
    'tt': "sop-triage",
    'cwt': "sop-consultation",
    'trt': "sop-treatment",
    'zt': "sop-zone-time",
    
    'redZone': 'sop-globe',
    'yellowZone': 'sop-globe',
    'greenZone': 'sop-globe',

    "admission": "sop-admission",
    "ane": "sop-er",
    "radiology": "sop-radiology",
    "discharge": "sop-suitcase",
    # "or": "sop-ot-2",
    "or": "sop-cpr",
    "pharmacy": "sop-pharmacy",
    "facilities": "sop-facilities",
    'crm': "sop-security-pass",
    'ias': "sop-ias",
    'prm': 'sop-user-folder',

    'visit': 'sop-identification-documents',
    'triageStart': 'sop-nurse',
    'triageEnd': 'sop-audit',
    'consultation': 'sop-medical-doctor',
    'discharge': 'sop-suitcase',
    'billClr': 'sop-bill',

    'pending': 'sop-sand-watch',
    'med-enquiry': 'sop-ask-question',
    'cost': 'sop-money-bag',
    'process': 'sop-process',
    'pain': 'sop-pain',
    'cancelled': 'sop-cancel',
    
    'bed-occupied': 'sop-bed-user',
    'bed-available': 'sop-bed-waiting',
    'bed-operational': 'sop-bed-user',
    'bed-fumigation': 'sop-bed-cpr',

    'bookmark': 'sop-bookmark-2',
    'task-plan': 'sop-task-planning-2',
    'tick-cross': 'sop-tick-cross',

    'queue': 'sop-icons8-joining-queue--1--1-50',
    'laboratory': 'sop-laboratory',
    'Lab': 'sop-laboratory',
    'Radiology': 'sop-radiology',
    'other': 'sop-view-more',
    'Other': 'sop-hospital-insurance',
}

# {"ane": "CC5050", "radiology": "6174B7", "admission": "8B4367","discharge":"E57E10","or":"F2538C","pharmacy":"343571","facilities":"18788C"}
HOME_JSON_STRUCT = {}
HOME_JSON_STRUCT['ane'] = {"title": "ER", "card":{}, "detail":{}, "enabled": True, "icon": ICONS['ane'], "color": "#853C79","kpi":3600}
HOME_JSON_STRUCT['radiology'] = {"title": "Radiology", "card":{}, "detail":{}, "enabled": True, "icon": ICONS['radiology'], "color": "#2c4077","kpi":7200}
HOME_JSON_STRUCT['admission'] = {"title": "Admission", "card":{}, "detail":{}, "enabled": False, "icon": ICONS['admission'],"kpi":5400}
HOME_JSON_STRUCT['discharge'] = {"title": "Discharge", "card":{}, "detail":{}, "enabled": False, "icon": ICONS['discharge'],"kpi":7200}
HOME_JSON_STRUCT['or'] = {"title": "Operation Room", "card":{}, "detail":{}, "enabled": False, "icon": ICONS['or'],"kpi":5400}
HOME_JSON_STRUCT['pharmacy'] = {"title": "Pharmacy", "card":{}, "detail":{}, "enabled": False, "icon": ICONS['pharmacy'],"kpi":3600}
HOME_JSON_STRUCT['facilities'] = {"title": "Facilities", "card":{}, "detail":{}, "enabled": False, "icon": ICONS['facilities'],"kpi":3600}

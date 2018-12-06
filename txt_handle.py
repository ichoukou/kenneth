from elasticsearch import Elasticsearch
from WorkItem.读取文件目录.elasticsearch_type import PatentType
import os

client = Elasticsearch(hosts=['127.0.0.1'])

path = 'FM'
for dirpath, dirname, filenames in os.walk(path):
    for name in filenames:
        txtpath = os.path.join(dirpath, name)
        if txtpath.endswith("txt"):
            #print(txtpath)
            f = open(txtpath, 'rt', newline="")
            # for meiduan in f.readlines():
            #     print(meiduan)
            data = f.readlines()
            patent = {}
            patent['patent_number'] = data[1].split(">=")[1]
            patent['application_number'] = data[2].split(">=")[1]
            patent['filing_date'] = data[3].split(">=")[1]
            patent['public_number'] = data[4].split(">=")[1]
            patent['open_day'] = data[5].split(">=")[1]
            patent['main_classification_number'] = data[6].split(">=")[1]
            patent['classification_number'] = data[7].split(">=")[1]
            patent['patent_name'] = data[8].split(">=")[1]
            patent['applicant'] = data[9].split(">=")[1]
            patent['inventor'] = data[10].split(">=")[1]
            patent['address'] = data[11].split(">=")[1]
            patent['country_code'] = data[12].split(">=")[1]
            patent['agency'] = data[13].split(">=")[1]
            patent['agent'] = data[14].split(">=")[1]
            patent['priority_number'] = data[15].split(">=")[1]
            patent['priority_day'] = data[16].split(">=")[1]
            patent['international_application'] = data[17].split(">=")[1]
            patent['international_publish'] = data[18].split(">=")[1]
            patent['date_of_entry'] = data[19].split(">=")[1]
            patent['separate_application'] = data[20].split(">=")[1]
            patent['legal_state'] = data[21].split(">=")[1]
            patent['source_item'] = data[22].split(">=")[1]
            patent['family_patent'] = data[23].split(">=")[1]
            patent['abstract'] = data[24].split(">=")[1]
            patent['keyword'] = data[25].split(">=")[1]
            patent['patent_type'] = data[26].split(">=")[1]
            patent['clan_number'] = data[27].split(">=")[1]
            patent['principal_claim'] = data[28].split(">=")[1]
            patent['priority_right'] = data[29].split(">=")[1]
            patent['patent_status'] = data[30].split(">=")[1]
            patent['status_code'] = data[31].split(">=")[1]


            espatent = PatentType()
            espatent.patent_number = patent['patent_number']
            espatent.application_number = patent['application_number']
            espatent.filing_date = patent['filing_date']
            espatent.open_day = patent['open_day']
            espatent.main_classification_number = patent['main_classification_number']
            espatent.classification_number = patent['classification_number']
            espatent.patent_name = patent['patent_name']
            espatent.applicant = patent['applicant']
            espatent.inventor = patent['inventor']
            espatent.address = patent['address']
            espatent.country_code = patent['country_code']
            espatent.agency = patent['agency']
            espatent.agent = patent['agent']
            espatent.priority_number = patent['priority_number']
            espatent.priority_day = patent['priority_day']
            espatent.international_application = patent['international_application']
            espatent.international_publish = patent['international_publish']
            espatent.date_of_entry = patent['date_of_entry']
            espatent.separate_application = patent['separate_application']
            espatent.legal_state = patent['legal_state']
            espatent.source_item = patent['source_item']
            espatent.family_patent = patent['family_patent']
            espatent.abstract = patent['abstract']
            espatent.keyword = patent['keyword']
            espatent.patent_type = patent['patent_type']
            espatent.clan_number = patent['clan_number']
            espatent.principal_claim = patent['principal_claim']
            espatent.priority_right = patent['priority_right']
            espatent.patent_status = patent['patent_status']
            espatent.status_code = patent['status_code']
            espatent.save()

            f.close()


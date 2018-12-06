from elasticsearch_dsl import DocType, Date, Nested, Boolean, analyzer, InnerObjectWrapper, \
    Completion, Keyword, Text, Integer, String
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])


class PatentType(DocType):
    patent_number = String()
    application_number = String()
    filing_date = String()
    public_number = String()
    open_day = String()
    main_classification_number = String()
    classification_number = String()
    patent_name = Text(analyzer="ik_max_word")
    applicant = Keyword()
    inventor = Keyword()
    address = Text(analyzer="ik_max_word")
    country_code = String()
    agency = String()
    agent = String()
    priority_number = String()
    priority_day = String()
    international_application = String()
    international_publish = String()
    date_of_entry = String()
    separate_application = String()
    legal_state = Text(analyzer="ik_max_word")
    source_item = String()
    family_patent = String()
    abstract = String()
    keyword = Text(analyzer="ik_max_word")
    patent_type = String()
    clan_number = String()
    principal_claim = String()
    priority_right = String()
    patent_status = Keyword()
    status_code = String()


    class Meta:
        index = "zhiguolian"
        doc_type = "patent"

if __name__ == "__main__":
    PatentType.init()






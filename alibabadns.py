from alibabacloud_alidns20150109.client import Client as DnsClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as dns_models


from config import config


class AlibabaDns:
    def __init__(self):
        pass

    @staticmethod
    def initialization() -> DnsClient:
        alibabacloud_config = open_api_models.Config(
            access_key_id=config.get("alibabacloud", "access_key_id"),
            access_key_secret=config.get("alibabacloud", "access_key_secret"),
        )
        alibabacloud_config.endpoint = config.get("alibabacloud", "endpoint")
        return DnsClient(alibabacloud_config)

    @staticmethod
    def add_domain_record(
        domain: str,
        rr: str,
        type: str,
        value: str,
    ) -> None:
        client = AlibabaDns.initialization()
        add_domain_record_request = dns_models.AddDomainRecordRequest(
            domain_name=domain, rr=rr, type=type, value=value
        )
        client.add_domain_record(add_domain_record_request)

    @staticmethod
    def delete_domain_records(
        domain: str,
        rr: str,
    ) -> None:
        client = AlibabaDns.initialization()
        delete_domain_records_request = dns_models.DeleteSubDomainRecordsRequest(
            domain_name=domain,
            rr=rr,
        )
        client.delete_sub_domain_records(delete_domain_records_request)

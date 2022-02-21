import json
import requests

from config import config


class NameComDNS:
    def __init__(self):
        pass

    @staticmethod
    def describe_domain_records(
        domain: str,
    ) -> json:
        url = "https://api.name.com/v4/domains/%s/records" % domain
        req = requests.get(
            url,
            auth=(
                config.get("namecomdns", "username"),
                config.get("namecomdns", "token"),
            ),
        )
        return req.json()["records"]

    @staticmethod
    def add_domain_record(
        domain: str,
        rr: str,
        type: str,
        value: str,
    ) -> None:
        data = {
            "domainName": domain,
            "host": rr,
            "type": type,
            "answer": value,
            "ttl": 300,
        }
        url = "https://api.name.com/v4/domains/%s/records" % domain
        req = requests.post(
            url,
            data=json.dumps(data),
            auth=(
                config.get("namecomdns", "username"),
                config.get("namecomdns", "token"),
            ),
        )
        if req.status_code == 200 or req.status_code == 201:
            return
        else:
            raise Exception(
                "name.com API %s Error: %s" % (req.status_code, req.content)
            )

    @staticmethod
    def delete_domain_records(
        domain: str,
        rr: str,
    ) -> None:
        for record in NameComDNS.describe_domain_records(domain):

            if record["host"] == rr:
                print(rr)
                url = "https://api.name.com/v4/domains/%s/records/%s" % (
                    domain,
                    record["id"],
                )
                req = requests.delete(
                    url,
                    auth=(
                        config.get("namecomdns", "username"),
                        config.get("namecomdns", "token"),
                    ),
                )
                if req.status_code == 200 or req.status_code == 201:
                    return
                else:
                    raise Exception(
                        "name.com API %s Error: %s" % (req.status_code, req.content)
                    )

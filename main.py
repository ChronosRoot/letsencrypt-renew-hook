#!/usr/bin/env python

import sys, os
from typing import List
import logging
import logging.handlers

from alibabadns import AlibabaDns
from namedns import NameComDNS

rr = "_acme-challenge"

logger = logging.getLogger("logger")
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
consoleHandler = logging.StreamHandler(stream=sys.stdout)
logger.setLevel(logging.DEBUG)
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)


def auth(module: str):
    try:
        if "CERTBOT_DOMAIN" not in os.environ:
            raise Exception("Environment variable CERTBOT_DOMAIN is empty.")
        if "CERTBOT_VALIDATION" not in os.environ:
            raise Exception("Environment variable CERTBOT_VALIDATION is empty.")

        domain = os.environ["CERTBOT_DOMAIN"]
        value = os.environ["CERTBOT_VALIDATION"]

        if module in ("alibabadns"):
            AlibabaDns.add_domain_record(domain, rr, type="TXT", value=value)
        elif module in ("namecomdns"):
            NameComDNS.add_domain_record(domain, rr, type="TXT", value=value)
        else:
            logger.error(str(e))
            sys.exit()

    except Exception as e:
        logger.error(str(e))
        sys.exit()


def cleanup(module: str):
    try:
        if "CERTBOT_DOMAIN" not in os.environ:
            raise Exception("Environment variable CERTBOT_DOMAIN is empty.")

        domain = os.environ["CERTBOT_DOMAIN"]
        logger.info("Start to clean up")
        logger.info("Domain:" + domain)

        if module in ("alibabadns"):
            AlibabaDns.delete_domain_records(domain, rr)
        elif module in ("namecomdns"):
            NameComDNS.delete_domain_records(domain, rr)
        else:
            logger.error(str(e))
            sys.exit()

    except Exception as e:
        logger.error(str(e))
        sys.exit()


def main(
    args: List[str],
) -> None:
    try:
        module = args[0]

        if args[1] in ("--auth"):
            auth(module)
        elif args[1] in ("--cleanup"):
            cleanup(module)
        else:
            logger.error("Invalid option: " + args[1])

    except Exception as e:
        logger.error(str(e))

        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])

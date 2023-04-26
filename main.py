import json
import requests
import xmltodict
import sentry_sdk
import config as cfg

# Sentry configuration
sentry_sdk.init(
    dsn=cfg.SENTRY_DSN,
    traces_sample_rate=1.0,
)

auth = (cfg.FACTUREAZA_RO_API_KEY, 'x')


def process_invoice():
    url = cfg.FACTUREAZA_RO_API_URL + '/invoices.xml'
    response = requests.get(url, auth=auth, verify=False)

    if response.status_code != 200:
        raise Exception("Error fetching invoices")

    invoices_xml = response.content
    invoices_dict = xmltodict.parse(invoices_xml)
    invoices_json = json.dumps(invoices_dict, indent=4)

    return invoices_json


if __name__ == "__main__":
    invoices = process_invoice()
    print(invoices)

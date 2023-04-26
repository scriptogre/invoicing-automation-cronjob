import json
import requests
import xmltodict
import sentry_sdk

from fastapi import FastAPI, HTTPException

from config import FACTUREAZA_RO_API_URL, FACTUREAZA_RO_API_KEY, SENTRY_DSN

# Sentry configuration
sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
)

auth = (FACTUREAZA_RO_API_KEY, 'x')

app = FastAPI()


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


@app.get("/invoices")
def process_invoice():
    url = FACTUREAZA_RO_API_URL + '/invoices.xml'
    response = requests.get(url, auth=auth, verify=False)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching invoices")

    invoices_xml = response.content
    invoices_dict = xmltodict.parse(invoices_xml)
    invoices_json = json.dumps(invoices_dict, indent=4)

    return invoices_json

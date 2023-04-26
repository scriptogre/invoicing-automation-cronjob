# Make sure Sentry is initialized before importing any other code
import sentry_config

import json
import requests
from fastapi import FastAPI, HTTPException
import xmltodict

from config import FACTUREAZA_RO_API_URL, FACTUREAZA_RO_API_KEY

app = FastAPI()

auth = (FACTUREAZA_RO_API_KEY, 'x')


@app.get("/invoices")
def process_invoice():
    url = FACTUREAZA_RO_API_URL + 'invoices.xml'
    response = requests.get(url, auth=auth, verify=False)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching invoices")

    invoices_xml = response.content
    invoices_dict = xmltodict.parse(invoices_xml)
    invoices_json = json.dumps(invoices_dict, indent=4)

    return invoices_json

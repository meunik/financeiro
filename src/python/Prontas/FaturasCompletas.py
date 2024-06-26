import sys
import json
from pynubank import Nubank, MockHttpClient

# python FaturasCompletas.py "../../public/cert.p12" 12345678910 123456 "../../database/json/nubank/FaturasCompletas.json"

cert = sys.argv[1]
cpf = sys.argv[2]
password = sys.argv[3]
caminhoArquivo = sys.argv[4]

# nu = Nubank(MockHttpClient())
nu = Nubank()
nu.authenticate_with_cert(cpf, password, cert)

bills = nu.get_bills()
dados = []
for bill in bills:
    if 'self' in bill['_links']:
        bill_details = nu.get_bill_details(bill)
        dados.append(bill_details)

with open(f'{caminhoArquivo}.json', 'w', encoding='utf-8') as f: json.dump(dados, f)

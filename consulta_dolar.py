import requests
from datetime import datetime, timedelta

def cotar(data):
    url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
    try:
        res = requests.get(url)
        res = res.json()
        if res.get('value'):
            return res['value'][0]['cotacaoCompra']
        return None
    except Exception:
        return None

data = input("Digite sua data no formato mm-dd-aaaa: ")
data_atual = datetime.strptime(data, "%m-%d-%Y")
data_final = data_atual + timedelta(days=365)

print(f"\nBuscando cotações diárias de {data_atual.strftime('%d/%m/%Y')} até {data_final.strftime('%d/%m/%Y')}:\n")

cont = data_atual
while cont <= data_final:
    cada_dia = cont.strftime("%m-%d-%Y")
    cotacao = cotar(cada_dia)

    if cotacao is not None:
        print(f"Data: {cont.strftime('%d/%m/%Y')} | Cotação Compra: {cotacao}")
    else:
        print(f"Data: {cont.strftime('%d/%m/%Y')} | Sem cotação (Fim de semana ou Feriado)")

    cont += timedelta(days=1)
# kutuphane
import requests

# veri girisleri
genel_api = 'https://api.genelpara.com/embed/doviz.json'
# bu genel degerleri gosteriyor
banka_api = 'https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/'
# bu bankalarda olan ortalama degerleri gosteriyor
dolar = 'USD'
euro = 'EUR'

# genel api ciktilari
def genel_alis_all_data(para):
    genel_data = requests.get(genel_api).json()
    return genel_data[para.upper()]

def banka_alis_all_data(para):
    banka_data = requests.get(f'{banka_api}{para.lower()}').json()
    return banka_data

# direkt degere yonelik fonksiyonlar
def genel_alis(para):
    genel_data = requests.get(genel_api).json()
    return genel_data[para.upper()]['alis']

def genel_satis(para):
    genel_data = requests.get(genel_api).json()
    return genel_data[para.upper()]['satis']

def banka_alis(para):
    banka_data = requests.get(f'{banka_api}{para.lower()}').json()
    return banka_data['BanknoteSelling']

def banka_satis(para):
    banka_data = requests.get(f'{banka_api}{para.lower()}').json()
    return banka_data['BanknoteBuying']

# Cikti
print(f'''
Dolar Alım: {genel_alis(dolar)},
Dolar Satım: {genel_satis(dolar)},
Dolar Banka Alım: {banka_alis(dolar)},
Dolar Banka Satım: {banka_satis(dolar)},
Euro Alım: {genel_alis(euro)},
Euro Satım: {genel_satis(euro)},
Euro Banka Alım: {banka_alis(euro)},
Euro Banka Satım: {banka_satis(euro)},
--
Genel Dolar Alım API Çıktısı: {genel_alis_all_data(dolar)},
Banka Dolar Alım API Çıktısı: {banka_alis_all_data(dolar)}.
''')

import requests

def calc_juros_simples(capital, taxa_percentual, tempo_anos):
    taxa = taxa_percentual / 100
    juros = capital * taxa * tempo_anos 
    return round(juros, 2)

def calc_juros_compostos(capital, taxa_percentual, tempo_anos):
    taxa = taxa_percentual / 100
    montante = capital * (1 + taxa) ** tempo_anos 
    juros = montante - capital
    return round(juros, 2)

def calc_desconto(preco, desconto):
    return preco - (preco * (desconto/100))

def cotacao(moeda_origem, moeda_destino):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}'
    response = requests.get(url)

    if response.status_code == 200:
        dados_recebidos = response.json()
        chave = f'{moeda_origem}{moeda_destino}'
        if chave in dados_recebidos:
            return float(dados_recebidos[chave]['bid'])
        else:
            print(f'ERROR! Par de moedas {moeda_origem}-{moeda_destino} não encontradas!')
    else:
        print(f'ERROR! Status code: {response.status_code}')
        return None

def menu():
    print('---- MENU DE SELEÇÃO ---- \n')
    print('Selecione o que deseja fazer: ')
    print('(1) Converter moedas')
    print('(2) Calcular juros simples')
    print('(3) Calcular juros compostos')
    print('(4) Calcular desconto')
    print('(5) Sair')


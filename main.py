from biblioteca_financas.financas import cotacao, calc_juros_simples, calc_juros_compostos, calc_desconto, menu

while True:
    menu()
    opcao = int(input('Seleciona uma opção: '))
    match opcao:
        case 1:
            print('---- CONVERSOR DE MOEDAS ----\n')
            moeda_origem = input('Digite a sigla da primeira moeda (Ex: BRL): ').upper()
            moeda_destino = input('Digite a sigla da segunda moeda (Ex: USD): ').upper()
            
            try:
                valor = float(input(f'Insira o valor a ser convertido {moeda_origem}: '))
            except:
                print('Valor inválido! Tente novamente:')
                continue

            cotacao_atual = cotacao(moeda_origem, moeda_destino)

            if cotacao_atual:
                valor_convertido = valor * cotacao_atual
                print(f'{valor} {moeda_origem} equivale a {valor_convertido:.2f} {moeda_destino}')
            else:
                print('Não foi possível obter a cotação!')
        case 2:
        
            print('---- CALCULO JUROS SIMPLES ----\n')
            try:
                capital = float(input('Insira o valor do capital: '))
                taxa_percentual = float(input('Insira a taxa (%): '))
                tempo_anos = float(input('Insira o tempo em anos: '))
                juros = calc_juros_simples(capital, taxa_percentual, tempo_anos)
                print(f'O Valor do juros a ser pago é : {juros}')
            except:
                print('Erro ao calcular juros simples!')
        case 3:
            print('---- CALCULO JUROS COMPOSTOS ----\n')
            try:
                capital = float(input('Insira o valor do capital: '))
                taxa_percentual = float(input('Insira a taxa (%): '))
                tempo_anos = float(input('Insira o tempo em anos: '))
                juros_compostos = calc_juros_compostos(capital, taxa_percentual, tempo_anos)
                print(f'O Valor do juros compostos a ser pago é : {juros_compostos:.2f}')
            except:
                print('Erro ao calcular juros compostos!')
        case 4:
            print('---- CALCULAR DESCONTO ----\n')
            try:
                preco = float(input('Insira o valor inicial :'))
                desconto = float(input('Insira o desconto: '))
                preco_final = calc_desconto(preco, desconto)
                print(f'Preço final: R${preco_final:.2f}')
            except:
                print('Erro ao calcular o desconto')
        case 5:
            print('Finalizando o programa...')
            break
        case _:
            print('Seleção Inválida! Tente novamente: ')
            continue
        
    continuar = input('Deseja continuar (s/n): ').lower()
    if continuar != 's' and continuar != 'sim':
        print('Programa Finalizado')
        break
import time

opcao = -1
carros_disponiveis = []

while opcao != 5:
    print('\nSeja bem-vindo à Tavares Veículos.')
    time.sleep(1)

    print('\n1) Ver carros disponíveis em estoque.')
    print('2) Adicionar carro ao estoque.')
    print('3) Pesquisar carros com base no seu código.')
    print('4) Remover carro do estoque.')
    print('5) Sair.')

    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
            break
        except ValueError:
            print('Valor inválido! Tente novamente.')

    if opcao == 1:
        print('\nNo momento, os carros disponíveis são:')
        if len(carros_disponiveis) > 0:
            for i, carro in enumerate(carros_disponiveis, start=1):
                print(f"{i}. {carro}")
        else:
            print('Não há carros disponíveis no momento.')
    elif opcao == 2:
        new_car = input('Qual carro você deseja adicionar ao estoque? ')
        if len(new_car) > 0:
            carros_disponiveis.append(new_car)
            print(f'O carro "{new_car}" foi adicionado ao estoque com sucesso!')
        else:
            print('Nenhum carro foi adicionado.')
    elif opcao == 3:
        print('Pesquise o carro pelo código correspondente.')
        find = int(input('Digite o código do carro que deseja consultar: '))

        if 1 <= find <= len(carros_disponiveis):
            carro = carros_disponiveis[find - 1]
            print(f'{find}) {carro}')
        else:
            print('Código inválido! Tente novamente.')
    elif opcao == 4:
        print("Qual carro será removido hoje?")

        for i, carro in enumerate(carros_disponiveis, start=1):
            print(f"{i}) {carro}")

        remove_car = int(input('Digite o código do carro que deseja remover: '))

        if 1 <= remove_car <= len(carros_disponiveis):
            carro_removido = carros_disponiveis.pop(remove_car - 1)
            print(f'O carro "{carro_removido}" foi removido com sucesso!')
        else:
            print('Código inválido! Tente novamente.')
    elif opcao == 5:
        print("\nSaindo do sistema...")
        time.sleep(1)
        print('\nObrigado. Volte sempre!')
    else:
        print('O número digitado não corresponde às opções cadastradas no sistema.')

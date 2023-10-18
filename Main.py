# Calculadora Simples
from calculadora import soma

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora Simples --\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Sair')

    # Escolha do usuário
    op = int(input('\n\t\t\tOpção: '))

    # Processamento
    if op == 1:
            print('\n\t\t\t Soma \n')

    # Entrada
    n1 = int(input('Informe n1: '))
    n2 = int(input('Informe n2: '))

    # Processamento
    total = soma(n1, n2)

    # Saída
    print(f'\n\n\t{n1} + {n2} = {total}\n')
    if op == 2:
        print('\n\t\t\t Subtração \n')

    # Entrada

    # Processamento

    # Saída

    if op == 3:
        print('\n\tForte Abraço!!!\n')
        break
    else:
        print(f'\nA opção {op} está incorreta.\n')
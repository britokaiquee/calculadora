import os
from formula_brito_beta import formula_brito as fb


while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: '
            )

        if entrada.lower() == 'i':
            print('\nCalculadora 6.0\n')
            resultado = float(input('Primeiro número:\n'))

            while True:
                operador = input('Operador (ou "F" para finalizar):\n')

                if operador.lower() == 'f':
                    break

                if operador in ['+', '-', '*', '/', '//', '**', '%', '%%']:
                    num = float(input('\nPróximo número:\n'))
                    if operador == '+':
                        resultado += num
                    elif operador == '-':
                        resultado -= num
                    elif operador == '*':
                        resultado *= num
                    elif operador == '/':
                        resultado /= num
                    elif operador == '//':
                        resultado //= num
                    elif operador == '**':
                        resultado **= num
                    elif operador == '%':
                        resultado %= num
                    elif operador == '%%':
                        print(
                            f'\nResultado:\
                            \n{fb(int(resultado), int(num))}'
                            )

                else:
                    print('Erro: operador inválido.')
                    continue

                if resultado.is_integer():
                    resultado = int(resultado)
                    os.system('cls')
                    print(f'\nResultado: {resultado}\n')

        elif entrada.lower() == 'p':
            print('\nPrograma encerrado.')
            break

        else:
            print('Erro: você não digitou nenhuma das opções.')

    except ValueError:
        print('Erro: valor inválido.')

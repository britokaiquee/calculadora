import os
from formula_brito_beta import formula_brito as fb


def limpar_tela():
    # Função para limpar a tela, compatível com Windows e Unix-based OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: '
        )
        limpar_tela()

        if entrada.lower() == 'i':
            print('\nCalculadora 7.0\n')
            while True:
                try:
                    resultado = float(input('Primeiro número:\n'))
                    break  # Sai do loop se o valor for válido
                except ValueError:
                    limpar_tela()
                    print('\nErro: valor inválido. Tente novamente.\n')
            print()

            while True:
                operador = input('Operador (ou "F" para finalizar):\n')

                if operador.lower() == 'f':
                    break

                if operador in ['+', '-', '*', '/', '//', '**', '%', '%%']:
                    while True:
                        try:
                            num = float(input('\nPróximo número:\n'))
                            if num == 0:
                                if operador == '/' or operador == '//' \
                                    or operador == '%%':
                                    print('\nErro: divisão por zero.')
                                    continue
                            break  # Sai do loop se o valor for válido
                        except ValueError:
                            limpar_tela()
                            print('\nErro: valor inválido. Tente novamente.\n')

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
                        limpar_tela()
                        print(
                            f'\nResultado:\
                                \n{fb(int(resultado), int(num))}'
                        )
                        break

                    if resultado.is_integer():
                        resultado = int(resultado)

                    print(f'\nResultado: {resultado}\n')

                else:
                    print('\nErro: operador inválido.\n')

        elif entrada.lower() == 'p':
            print('\nPrograma encerrado.')
            break

        else:
            print('Erro: você não digitou nenhuma das opções.')

    except ValueError:
        limpar_tela()
        print('Erro: valor inválido.')
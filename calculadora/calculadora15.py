import os
import sys
from formula_brito import divisao_equilibrada, lista_comandos, radiciacao


print('Calculadora 15.0\n')

operadores = ['+', '-', '*', '**', '/', '//', '%', '%%', '&']

# Lista para armazenar o histórico das operações
historico = []


def main():
    while True:
        # Solicita o primeiro número
        numero = obter_numero('Primeiro número:\n')

        while True:
            operador = input('\nOperador/comando ("L" para listar):\n').lower()

            switch_comando = {
                'l': lista_comandos,
                'p': sys.exit,
                'h': exibir_historico,
                'r': lambda: (historico.clear(), limpar_tela(), \
                            print('Histórico apagado.')),
            }

            if operador == 'f':
                limpar_tela()
                break

            elif operador in switch_comando:
                switch_comando[operador]()
                continue

            # Verifica se o operador é válido antes de continuar
            if operador not in operadores:
                limpar_tela()
                print('\nOperador ou comando inválido. Tente novamente.')
                continue

            # Solicita o próximo número
            prox_num = obter_numero('\nPróximo número:\n')

            # Executa a operação e atualiza o número
            resultado = executar_operacao(numero, operador, prox_num)

            limpar_tela()
            print(f'Resultado:\n{resultado}')

            if operador == '%%':
                break

            # Atualiza o número para a próxima iteração
            numero = resultado


# Função para obter um número do usuário com tratamento de erro
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            limpar_tela()
            print('\nValor inválido. Tente novamente.')


# Função para executar a operação matemática
def executar_operacao(x, operador, y):
    # Dicionário de operadores e suas funções correspondentes
    switch_operador = {
        '+': lambda: x + y,
        '-': lambda: x - y,
        '*': lambda: x * y,
        '**': lambda: x ** y,
        '/': lambda: x / y,
        '//': lambda: x // y,
        '%': lambda: x % y,
        '%%': lambda: divisao_equilibrada(
            formatar(x), formatar(y), 
            input('\nNome e/ou separador (ou enter): ') or 'x',
            input('Nome 2 (ou enter): ') or ''
            ),
        '&': lambda: radiciacao(x, y)
    }

    try:
        if operador in switch_operador:
            resultado = switch_operador[operador]()
            # Verificação para evitar floats desnecessários
            resultado = formatar(resultado)
            # Adiciona a operação ao histórico
            historico.append((formatar(x), operador, formatar(y), resultado))
            return resultado

    except ZeroDivisionError:
        return '\nErro: é impossível dividir por zero.'


# Função para verificar se o número é inteiro ou float
def formatar(numero):
    if isinstance(numero, float) and numero.is_integer():
        return int(numero)
    return numero


# Função para exibir o histórico das operações
def exibir_historico():
    limpar_tela()
    print('\nHistórico das operações:')
    for i, operacao in enumerate(historico, 1):
        num_anterior, op, prox_num, resultado = operacao
        print(f'\n{i}. {num_anterior} {op} {prox_num} = {resultado}')


# Função para limpar a tela, compatível com Windows e Unix-based OS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
# n = divideNdo | d = Divisor | q = Quociente | r = Resto | a = Adição (próximo 
# número após o do quociente)

# nn = nome pro valor do dividendo e/ou separador ("x" remete ao sinal de 
# multiplicação, e é o argumento padrão para o separador)

# dd = nome pro valor do divisor


# Versão definitiva

def divisao_equilibrada(n, d, nn='x', dd=''):
    q = n // d
    r = n % d
    a = q + 1

    if r == 0:
        return f'{q} {nn} {d} {dd}'
    
    if isinstance(n, float) or isinstance(d, float):
        q = n / d
        return f'{q} {nn} {d} {dd}'

    return f'\n{q} {nn} {(d - r)} {dd}\n{a} {nn} {r} {dd}'


# teste_resultado = divisao_equilibrada(10, 3)
# print(teste_resultado)


def lista_comandos():
    print('\nOperadores disponíveis:')
    print(' +  : Adição')
    print(' -  : Subtração')
    print(' *  : Multiplicação')
    print(' ** : Exponenciação')
    print(' /  : Divisão')
    print(' // : Divisão inteira')
    print(' %  : Módulo')
    print(' %% : Divisão equilibrada')
    print('\nDica para calcular uma raiz quadrada:')
    print('Operador: **\nPróximo número: 0.5')
    print('\nPara calcular com outras potências, troque 0.5 pelo resultado')
    print('da divisão de 1 pelo número da potência que você quer.\n')

    print('\nComandos disponíveis:')
    print(' L  : Exibir lista de operadores e comandos disponíveis')
    print(' H  : Histórico da operação')
    print(' R  : Resetar histórico')
    print(' F  : Finalizar operação')
    print(' P  : Parar/encerrar o programa')

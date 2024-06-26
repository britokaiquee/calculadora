# Versão beta (da versão 6.0 da calculadora até a 12.0)

def formula_brito(n, d, nn='x', dd=''):
    q = n // d
    r = n % d

    if r == 0:
        return f'{q} {nn} {d} {dd}'

    return f'{q} {nn} {(d - r)} {dd}\n{(q + 1)} {nn} {r} {dd}'


# # Testes:
# resultado = formula_brito(10, 3, 'biscoito(s) para', 'pessoa(s)')
# print(resultado)


'''
n = divideNdo | d = Divisor | q = Quociente | r = Resto | x = resultado

nn = nome pro valor do dividendo + separador ("x" é o argumento padrão para
o separador)

dd = nome pro valor do divisor
'''
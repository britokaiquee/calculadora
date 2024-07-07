# Operador criado por mim
def divisao_equilibrada(dividendo, divisor, n1='x', n2=''):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    next = quociente + 1

    if resto == 0:
        return f'{quociente} {n1} {divisor} {n2}'

    if isinstance(dividendo, float) or isinstance(divisor, float):
        quociente = dividendo / divisor
        return f'{quociente} {n1} {divisor} {n2}'

    return f'\n{quociente} {n1} {(divisor
                                  - resto)} {n2}\n{next} {n1} {resto} {n2}'
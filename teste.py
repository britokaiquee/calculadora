def formatar():
    indice = int(input('índice: '))
    radicando = int(input('radicando: '))
    potencia = 1 / indice
    raiz = radicando ** potencia

    if isinstance(raiz, float) and raiz.is_integer():
        return int(raiz)
    return raiz

conta = formatar()
print(conta)
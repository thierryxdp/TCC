def colchao(medidas, H, L):
    """Funcao que dadas as dimensoes de um colchao e a altura e a largura de uma porta, retorne a possibilidade de passar ou nao pela porta.
list, int, int --> bool
testes:
colchao([25, 120, 220], 200, 100) == True
colchao([25, 205, 220], 200, 100) == False
colchao([25, 200, 220], 200, 100) == True
H = altura da porta
L = largura da porta"""

    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    medidas = [a, b, c]
    if (b <= H) and (a <= L):
        return "True"
    elif (b <= L) and (a <= H):
        return "True"
    else:
        return "False"
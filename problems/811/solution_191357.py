def colchao(medidas,H,L):
    """Função que dado as dimensões de um colchão e a altura e largura de uma porta, retorna se é possível ou não
o colchão passar pela porta.
list, int, int --> bool
testes:
colchao([25,120,220], 200, 100) == True
colchao([25,205,220], 200, 100) == False
colchao([25,200,220], 200, 100) == True
H = altura da porta
L = largura da porta
"""
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    medidas = [a,b,c]
    if (b <= H) and (a <= L):
        return "True"
    elif (b <= L) and (a <= H):
        return "True"
    else:
        return "False"
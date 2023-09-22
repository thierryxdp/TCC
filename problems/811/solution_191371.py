def colchao(medidas, H, L):
    """Recebe as dimensões (AxBxC) do colchao (em cm, da menor para maior)
em forma de lista e a altura e largura da porta como inteiros. Retorna True
se o colchao consgue passar pela porta e False se não passa pela porta.
assinatura: list, int, int --> bool
testes:
colchao([25, 120, 220], 200, 100) == True
colchao([30, 230, 100], 200, 100) == False
"""
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    medidas = [a, b, c]
    
    if (b <= H) and (a <= L):
        return True 
    elif (b <= L) and (a <= H):
        return True
    else:
        return False
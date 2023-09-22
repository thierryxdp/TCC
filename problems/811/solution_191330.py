def colchao(medidas, H, L):
    """Recebe as dimensões (AxBxC) do colchao (em cm, da menor para maior)
em forma de lista e a altura e largura da porta como inteiros. Retorna True
se o colchao consgue passar pela porta e False se não passa pela porta.
assinatura: list, int, int --> bool
testes:
colchao([25, 120, 220], 200, 100) == True
"""
    if (medidas[0][1] <= medidas[1]):
        return True
    else:
        return False
def colchao(lista,H,L):
    """Dados uma lista com as dimensões do colchão 
    ordenadas da menor para a maior e dois inteiros
    "H" e "L" representando a altura e largura da 
    porta respectivamente, retorna True se o colchão
    passa pelas portas e False se não passa
    list, float, float -> bool"""
    
    maior = max(L,H)
    menor = min(L,H)
    if lista[1] > maior:
        return False
    else:
        if lista[0] > menor:
            return False
        else:
            return True
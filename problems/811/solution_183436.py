# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ Essa função ajuda João a saber se ele consegue passar o ou não o colchão pelas portas de sua casa.

        Parameters:
        medidas = deve ser uma lista com as dimensões inteiras do colchão em centímetros, ordenadas da menor para a maior.
        H = altura inteira das portas em centímetros.
        L = largura inteira das portas em centímetros.

        Testes:
            colchao([25,120,220], 200, 100) = True
            colchao([25,205,220], 200, 100) = False
            colchao([25,200,220], 200, 100) = True

        Returns:
             A sua função deve retornar True se o colchão passa pelas portas e False caso contrário.
            list, int, int --> bool
    """
    espessura = medidas[1]
    largura = medidas[2]
    
    if (espessura <= H and largura < = L) or (espessura <= L and largura < = H):
        return True
    else:
        return False
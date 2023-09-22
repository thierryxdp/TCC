# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """A partir das 3 dimensões de um colchão, em centímetros, calcula se 
    será possível o colchão passar pela porta da casa de João;
    list, int, int -> bool"""  
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if (H>=B and L>=A):
        return True
    elif (L>=B and H>=A):
        return True
    elif (H>=C and L>=A):
        return True
    else:
        return False
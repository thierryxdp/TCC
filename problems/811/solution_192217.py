def colchao (medidas,H,L):
    '''função que retorna verdadeiro caso o colchao passe pela porta e falso caso não passe'''
    A,B,C = medidas
    if H >= A and L >= B or H >= B and L >= A:
        return True
    else:
        return False
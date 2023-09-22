#Mirella Maturo da Cruz DRE:119023985 Questão 7 do Laboratório 5[
def colchao (medidas,H,L):
    '''Retorna verdadeiro caso o colchao passe e falso caso nao passe'''
    
    if H>L:
        return medidas[0] <= L and medidas[1] <= H
    else:
        return medidas[0] <= H and medidas[1] <= L
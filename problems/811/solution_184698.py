# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''Descobre se um colchao com medidas A, B e C consegue passar por uma 
    porta de altura H e largura L. Recebe uma lista com as 3 medidas em 
    inteiros e as dimensoes da porta
    list, int,int->bool'''
    
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if A<=L and B<=H:
        return True
    elif B>=H and C<=L and A<=H
        return False
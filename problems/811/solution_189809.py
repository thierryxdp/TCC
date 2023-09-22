colchao(medidas,H,L):
    '''funcao que recebe uma lista medidas com as dimensoes de um colchao,
    e as dimensoes altura H e largura L da porta e retorna True se o colchao 
    passa pela porta ou False caso nao passe
    list,int,int->bool'''
    a = min(medidas)
    if (medidas[0]>medidas[1] and medidas[0]<medidas[2])or(medidas[0]>medidas[2] and medidas[0]<medidas[1]):
        b = medidas[0]
    if (medidas[1]>medidas[0] and medidas[1]<medidas[2])or(medidas[1]>medidas[2] and medidas[1]<medidas[1]):
        b = medidas[1]
    if (medidas[2]>medidas[0] and medidas[2]<medidas[1])or(medidas[2]>medidas[1] and medidas[2]<medidas[0]):
        b = medidas[2]
        
    if a<L and b<H:
        return True
    else:
        return False
def colchao(medidas,H,L):
    '''funcao que dado as dimensoes(AxBxC) em ordem crescente
de um colchao e a altura H e largura L de uma porta, retorna
True caso o colchao passe pela porta e false caso contrario;
list,float,float -> bool'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    #torna L menor que H
    if (L > H):
        aux = H
        H = L
        L = aux
    if (L >= A and H >= B):
        return True
    else:
        return False
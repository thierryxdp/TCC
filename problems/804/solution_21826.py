def filtra_pares(tupla):
    '''funçao que tem como entrada uma tupla de 4 elementos e saída uma tupla com elementos pares da tupla original; 
    int,int,int,int->tupla'''
    saida=()
    if tupla[0]%2==0:
        saida+=(tupla[0],)
    if tupla[1]%2==0:
        saida+=(tupla[1],)
    if tupla[2]%2==0:
        saida+=(tupla[2],)
    if tupla[3]%2==0:
        saida+=(tupla[3],)
    return saida
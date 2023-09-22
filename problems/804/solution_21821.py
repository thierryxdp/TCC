def filtra_pares (x,y,z,w):
    '''retorna um tupla contendo apenas os elementos pares da tupla original, na mesma oradem que se encontravam
    int,int,int,int->tuple'''
    saida=()
    if tupla[0]%2==0:
        saida+=(tupla[0],)
    if tupla[1]%2==0:
        saida+=(tupla[1],)
    if tupla[2]%2==0:
        saida+=(tupla[2],)
    if tupla[3]%2==0:
        saida+=(tupla[3],)
    return tupla(tupla[0],tupla[1],tupla[2],tupla[3])
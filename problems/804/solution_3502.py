def filtra_pares(tupla):  
    '''Filtra uma tupla de 4 elementos inteiros para retornar uma nova tupla com os elementos pares da tupla original
    entrada: tupla(int,int,int,int)
    saida: tupla(int,int,int,int)'''
    tp_vz = () 
    if tupla[0]%2==0:
        tp_vz = tp_vz + (tupla[0],)
    if tupla[1]%2==0:
        tp_vz = tp_vz + (tupla[1],)
    if tupla[2]%2==0:
        tp_vz = tp_vz + (tupla[2],)     
    if tupla[3]%2==0:
        tp_vz= tp_vz + (tupla[3],)
    return tp_vz
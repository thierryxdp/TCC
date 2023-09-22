def posLetra(string,letra,ocorrencia): 
    '''Dadas uma string, uma letra e um número retorna o indice da letra  daquela ocorrencia na string
    string,string,int -> int'''
    lets = list(string)
    indices = []
    c = 0
    while c < len(lets):
        if letra == lets[c]:
            indices.append(c)
        c+=1
    if ocorrencia <= len(indices):
        if ocorrencia <= 0:
            return -1
        return indices[ocorrencia-1]
    else:
        return -1
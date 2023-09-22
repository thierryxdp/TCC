def filtra_pares(tupla):
    """Retornar uma tupla contendo somente elementos inteiros como parâmentro e retorne uma tupla com apenas os elementos pares da tupla original;int,int,int,int=>tuple"""
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
#zip e for em lista
def repetidos(lista):
    '''retorna o numero de vezes que um 
    numero na lista e igual ao anterior;
    list -> int'''
    return list(for n in range(len(lista)): zip(n,n+1))
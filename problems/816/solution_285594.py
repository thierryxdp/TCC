def maiores(lista,num):
    '''retorna os numeros maiores que <num> contidos na lista
    lista,int->lista'''
    lista=lista+[num]
    lista.sort()
    lista=lista[(lista.index(num)+1):]
    
    return lista
def maiores(lista,inteiro):
    '''Função que retorna apenas os valores inteiros
    maiores que a entrada inteiro em forma de lista
    entrada=list,int
    saida=list'''
    x=list.append(lista,inteiro)
    h=list.sort(lista)
    y=list.index(lista,inteiro)
    g=lista[y+1::1]
    return g
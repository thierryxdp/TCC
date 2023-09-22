def faltante(lista):
    ''' rodando a lista e analisando os elementos dentro
    os elementos que estão faltando ele completa e se a lista
    estiver completa ele retorna o proximo número'''
    l=list(range(1,lista[-1]))
    i=0
    while i<len(l):
        if l[i] not in lista:
            return l[i]
        i+=1
    return lista[-1]+1
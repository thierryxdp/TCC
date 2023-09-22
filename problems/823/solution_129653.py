def faltante(lista):
    '''Função que dada uma lista de peças numeradas de 1 a N, retorna o número da peça que está faltando
    lista[int,...] -> int'''
    list.sort(lista)
    i=0
    if lista[0]!=1:
        return 1
    while i<len(lista)-1:
        if lista[i]==lista[i+1]-1:
            i+=1
        else:
            return lista[i]+1
    else:
        return len(lista)+1
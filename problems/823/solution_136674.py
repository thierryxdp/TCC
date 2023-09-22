def faltante(lista_numeros):
    '''Função que ajuda joãozinho a descobrir qual a peça de seu quebra cabeça
    está faltando. O quebra cabeça possui N peças, numeradas de 1 a N. Dado uma lista
    com N-1 elementos, os quais são números inteiros numerados de 1 a N, a função retorna
    o elemento que está faltando; lista->int'''
    list.sort(lista_numeros)
    i=0
    if len(lista_numeros)==1:
        if lista_numeros[0]!=1:
            return lista_numeros[0]-1
        else:
            return lista_numeros[0]+1
    else:
        while lista_numeros[i+1]-lista_numeros[i]==1:  
            i+=1
            return lista_numeros[i]-1
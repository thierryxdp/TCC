def faltante(lista_numeros):
    '''Função que ajuda joãozinho a descobrir qual a peça de seu quebra cabeça
    está faltando. O quebra cabeça possui N peças, numeradas de 1 a N. Dado uma lista
    com N-1 elementos, os quais são números inteiros numerados de 1 a N, a função retorna
    o elemento que está faltando; lista->int'''
    list.sort(lista_numeros)
    i=1
    while abs(lista_numeros[i]-lista_numeros[i-1]) == 1:
        i+=1
    return lista_numeros[i]-1
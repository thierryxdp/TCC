def faltante(numero_pecas):
    '''Função que ajuda joãozinho a descobrir qual a peça de seu quebra cabeça
    está faltando. O quebra cabeça possui N peças, numeradas de 1 a N. Dado uma lista
    com N-1 elementos, os quais são números inteiros numerados de 1 a N, a função retorna
    o elemento que está faltando; lista->int'''
    list.sort(numero_pecas)
    i=1
    while numero_pecas[i]-numero_pecas[i-1] == 1:
        i+=1
    return numero_pecas[i]-1
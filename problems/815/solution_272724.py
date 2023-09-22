def insere (lista_numero, n):
    '''Dada uma lista ordenada de números inteiros e um outro
        denominado n (que pecisa ser pocisionado na posição
        correta), retorne uma lista ordenada;
        list, int -> list'''
    lista = lista_numero.append (n)
    lista_numero.sort ()
    return lista_numero.sort (lista)
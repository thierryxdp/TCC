def insere (lista_numero, n):
    '''
       Função que recebe uma lista de numeros ordenada do
       menor pro maior (lista_numero) e um numero inteiro
       (n) e retorna o numero n na posição correta, de tal
       maneira que a lista continue ordenada;
       list, int -> list
    '''
    lista = lista_numero.append(n)
    return lista.sort()
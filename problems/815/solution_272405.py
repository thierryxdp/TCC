def insere(lista_num,n):
    ''''Recebe uma lista de numeros ordenada(crescente) e um numero inteiro e retorna a mesma lista, com o
    numero inserido de forma que a lista continue ordenada
    list,int ->list'''
    lista_num=list.append(lista_num,n)
    list.sort(lista_num)
    return lista_num
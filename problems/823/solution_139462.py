def faltante(lista):
    '''função que recebe uma lista l de tamanho n-1 e retorna qual
    número pertence ao intervalo [i,n] mas não a lista l
    list->int'''
   
    contando = 0
    lista_ordenada = sorted(lista)

    while contando < len(lista):
        if contando + 1 == lista_ordenada[contando]:
            contando += 1
        else:
            return contando + 1

    return contando + 1
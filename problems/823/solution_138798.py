def faltante(lista):
    '''dada uma lista de numeros, descubre numeros interios numerados de 1 a N que esteja façtando
    :param lista: list->list
    :return: int->int
    '''
    contador= 0
    listaordenada= sorted(lista)
    while contador < len(lista):
        if contador + 1 ==listaordenada[contador]:
            contador +=1
        else:
            return contador + 1
        
        return contador + 1
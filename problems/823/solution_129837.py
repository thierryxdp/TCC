def faltante(lista):
    '''Função que dada uma lista, verifica dentre os elementos, qual
    é o faltante. O uso do recurso 'break' teve como finalidade realizar
    o procedimento de saída do while mesmo sem nenhuma condição no else.
    Entrada: list
    Saída: int'''
    indice=0
    contador=1
    list.sort(lista)
    while indice != len(lista)-1:
        if contador==lista[indice]:
            indice+=1
            contador+=1
        else:
            break
    if contador==lista[-1]:
        return contador+1
    else:
        return contador
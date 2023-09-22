def filtraMultiplos(lista_num,num):
    '''funcao que recebe uma lista com numeros e um numero e 
       retorna uma lista com os numeros multiplos desse numero
       list, int -> list'''
    i=0
    l_div= []
    while i < len(lista_num):
        if lista_num[i]%num == 0:
            list.append(l_div,lista_num[i])
        i += 1
    return l_div
def maiores(lista_num,num1):
    '''Esta função retorna uma lista contendo todos os
    números inteiros da lista inserida (lista_num) 
    maiores que o número inteiro (num1) inserido.
    list(int) -> list(int)'''
    
    list.insert(lista_num,1,num1)
    list.sort(lista_num)   

    indice=list.index(lista_num,num1)
    maiores=lista_num[indice+1:]

    return maiores
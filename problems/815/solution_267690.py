def insere(lista_numero, n):
    '''dada uma lista crescente de números,retorna uma nova lista com o valor n na posição correta; (list,int)->list'''
    
    lista2=[n]
    lista3=lista2 + lista_numero
    list.sort(lista3)

    return lista3
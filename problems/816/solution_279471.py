def maiores(lista_num,num):
    '''função que recebe uma lista numérica (lista_num)e um
    número inteiro (num) e retorna uma nova lista que contenha
    os mesmos componentes da lista original maiores que o número
    inteiro (num);
    lista, int->lista'''
    lista_nova = lista_num[:]
    list.insert(lista_nova,0,num)
    list.sort(lista_nova)
    posicao = (list.index(lista_nova,num))+1
    lista_final = lista_nova[posicao:]
    return lista_final
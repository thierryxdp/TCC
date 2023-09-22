def insere(lista_numero,n):
    '''Esa função tem como objetivo, inserir o numero (n) na lista de numeros,
    na ordem crescente, list, int,list'''
    
    n_list = [n]
    lista = list.sort((lista_numero + n_list))
    return lista
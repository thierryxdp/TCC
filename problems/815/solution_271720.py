def insere(lista_numero,n):
    '''Função que recebe uma lista de ordem crescente e um inteiro
    e o coloca na ordem correta dele
    entrada=list,int
    saida=list'''
    y=list.insert(lista_numero,0,n)
    h=list.sort(lista_numero)
    return lista_numero
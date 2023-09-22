def insere(lista_numero,n):
    '''inserir um elemento novo na lista ordenada e manter a ordem;
    list -> list'''
  #lista = list.sort(lista_numero)
#list.sort(lista)

lista = list.insert(lista_numero,1,n)
ordem = list.sort(lista)

	return ordem
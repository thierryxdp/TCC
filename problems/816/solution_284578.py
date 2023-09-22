def maiores(lista_n,N):
    """Tem como objetivo receber uma lista e um número inteiro
    e retornar outra lista com todos os número da lista original
    que são maiores que n.
    lista,int > lista"""
    lista_completa = insert_sort_des(lista_n, N)
    sub_lista = [ elem for elem in lista_completa if elem > N ]
    return sub_lista
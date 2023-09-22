def maiores(lista_n,N):
    """Tem como objetivo receber uma lista e um número inteiro
    e retornar outra lista com todos os número da lista original
    que são maiores que n.
    lista,int > lista"""
    sub_lista = [ elem for elem in lista_completa if elem > N ]
    return sub_lista
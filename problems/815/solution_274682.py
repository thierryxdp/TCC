def insere(lista_numero,n):
    """Função que insere número inteiro numa lista e a organiza.
assinatura: list,int -> list
"""
    mo1= list.extend(lista_numero,[n])
    mo2= list.sort(lista_numero)
    return lista_numero
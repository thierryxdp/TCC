# Função que inclui n na lista e na ordem 
# n é um número inteiro qualquer 
# list, int-> list
def insere(lista_numero,n):
    """Função que insere o inteiro n na ordem da lista numérica"""
    """list,int->list"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero
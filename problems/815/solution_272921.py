# Função que inclui n na lista e na ordem 
# n é um número inteiro qualquer 
# list, int-> list
def insere(lista_numero,n):
    """Função que insere o inteiro n na ordem da lista numérica"""
    """list,int->list"""
    if lista_numero[0]>n:
        return [n]+lista_numero
    elif lista_numero[0]<n<lista_numero[1]:
        return lista_numero[0]+[n]+lista_numero[1:]
    elif lista_numero[1]<n<lista_numero[2]:
        return lista_numero[0:2]+[n]+lista_numero[2:]
    elif lista_numero[2]<n<lista_numero[3]:
        return lista_numero[0:3]+[n]+lista_numero[3:]
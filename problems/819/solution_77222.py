def filtraMultiplos(lista,num):
    """função que recebe uma lista de números e um número, e retorna uma lista com os números da lista original que são 
 divisíveis pelo número dado
 list,int---->list"""
    nova_lista = []
    cont = 0
    while cont < len(lista):
        if lista[cont]%num ==0:
            nova_lista = nova_lista + [lista[cont]]
        cont = cont + 1
    return nova_lista
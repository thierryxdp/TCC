def filtraMultiplos(lista, num):
    """função que filtra os múltiplos de um número
    lista, int -> lista"""
    divisao = ()
    contador = 0
    while contador < len(lista):
        if (lista[contador]%num)==0:
            divisao = divisao +(lista[contador])
        contador += + 1
    return list(divisao)
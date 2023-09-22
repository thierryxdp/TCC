def filtraMultiplos(lista,n):
    """Recebe uma lista de números e um número 'n' inteiro. Retorna uma
    nova lista com todos os números da primeira que forem divisíveis por 'n'.
    Assinatura: list, int -> list"""
    listafinal=[]
    num=0
    while num<len(lista):
        if lista[num]%n == 0:
            listafinal.append(lista[num])
            num += 1
    return listafinal
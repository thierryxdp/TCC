def filtraMultiplos(lista, numero):
    """funcao que filtra os multiplos de um numero n e retorna uma lista dos numeros divisiveis por n
    list, int -> list"""
    resultado = []
    x = 0
    while x <= len(lista)-1:
        if lista [x] % numero == 0:
            y = lista[x]
            list.append(resultado,y)
            x = x + 1
        elif x <= len(lista):
            lista[x]%numero !=0
            x= x+1
                
    return resultado
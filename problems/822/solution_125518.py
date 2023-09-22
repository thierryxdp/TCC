def repetidos(numeros):
    """Dado uma lista de números, retorna a quantidade equivalente de repetições
    dos números contidos na lista com o seus antecessores:
    list-->int"""
    numero=len(numeros)
    numeros_iguais=0
    i=0
    while i<numero:
        if numeros[i]==numeros[i-1]:
            numeros_iguais+=1
        i+=1
    return numeros_iguais
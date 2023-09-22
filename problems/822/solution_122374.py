def repetidos(lista):
    """retorna a quantidade de numeros repetidos em sequencia
    entrada: lista, Saída: inteiro"""
    i=0
    repetidos = []
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repetidos.append(lista[i])
        i=i+1
    return len(repetidos)
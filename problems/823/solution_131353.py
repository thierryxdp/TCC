def faltante(lista):
    """Recebe uma lista com N-1 inteiro e retorna o número inteiro deste 
    intervalo"""
    contador = 1
    resultado = 0
    while contador <= len(lista):
        if contador not in lista:
            resultado += contador
        contador = lista[contador-1]+1
    if resultado == 0:
        resultado += len(lista)+1
    return resultado
def filtraMultiplos(listan):
    """Função que recebe uma lista com uma lista de valores e um inteiro (n) e retorna outra lista com os valores divisíveis por n."""


    valores_lista = listan[0]
    inteiro = listan[1]
    divisiveis = []
    contador = 0
    
    while contador < len(valores_lista):

        if valores_lista[contador] % inteiro == 0:
            divisiveis.append(valores_lista[contador])

        contador+=1

    return divisiveis
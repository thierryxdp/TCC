def filtraMultiplos(numeros, divisor):
    """Função que dada uma lista de números, retorna uma 
    outra lista com os multiplos do 'divisor'
    list, float -> list"""
    if indice < len(numeros):
        indice = 0
		listaNumeros = []
        while numeros[indice]%divisor == 0:
            listaNumeros = list.append(listaNumeros, numeros[indice])
            indice += 1
        return listaNumeros
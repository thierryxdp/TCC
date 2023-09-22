def filtra_pares(numeros):
    """Função que recebe uma tupla com quatro elementos inteiro como parâmetro, e retorna uma nova tupla somente com os elementos pares da tupla original, na mesma ordem que se encontram; tupla -> tupla."""
    tupla = ()

    if numeros[0]%2 == 0:
        tupla = tupla + (numeros[0],)
    if numeros[1]%2 == 0:
         tupla = tupla + (numeros[1],)
    if numeros[2]%2 == 0:
        tupla = tupla + (numeros[2],)
    if numeros[3]%2 == 0:
        tupla = tupla + (numeros[3],)

    return tupla
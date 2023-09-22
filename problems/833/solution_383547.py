def conta_numero(numero,matriz):
    """A fução recebe uma matriz(lista) e um número(inteiro) na entrada e retorna quantas vezes aquele número 
    se repete na matriz, ela converte a matriz e o número em string para fazer a cpntagem. Na saída ela devolve 
    um número inteiro referente a repetição."""
    converteMatriz = str(matriz)
    converteNumero = str(numero)
    contagem = converteMatriz.count(converteNumero)
    return contagem
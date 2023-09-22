def uppCons (frase):
    """Retorna todas as consoantes de uma dada frase em caixa alta.
    Entrada: str
    Saída: str
    """
    resultado = ''
    indice = 0
    while frase[indice] < len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            resultado = resultado + frase[indice]
            indice = indice + 1
    return resultado
def uppCons (frase):
    """Retorna todas as consoantes de uma dada frase em caixa alta.
    Entrada: str
    Saída: str
    """
    indice = 0
    while indice < len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            str.replace(frase, frase[indice], str.upper(frase[indice])
        indice = indice + 1
    return frase
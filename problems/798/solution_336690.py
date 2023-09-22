def freq_palavras(frases):
    """Dada uma frase, a função retorna um discionário
    contendo cada palavra dessa frase e a quantidade
    de vezes que ela aparece.
    Parametros de Entrada: string
    Retorna: dicionario"""

    dicionario={}
    auxiliar= frases.split('')

    for palavra in auxiliar:
        if palavra in auxiliar:
            dicionario[palavra]=str(list.count(auxiliar,palavra))
    return dicionario
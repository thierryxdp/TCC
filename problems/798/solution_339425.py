def freq_palavras(frase):
    """Retorna um dicionario onde cada chave eh
    uma palavra e tem como valor as ocorrencias
    dessa chave.
    str -> dict"""
    fs = frase.split()
    dicionario = {}
    for i in fs:
      dicionario[i] = fs.count(i)
    return dicionario
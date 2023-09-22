def freq_palavras(frases):
    """Recebe uma frase e retorna um dicionario contando
    quantas vezes cada palavra é repetida na frase"""
    texto = str.split(frases)
    dicionario = {}
    for var in texto:   
        n=str.count(texto,var)
        if var not in dicionario:
            dicionario[var] = n
    return dicionario
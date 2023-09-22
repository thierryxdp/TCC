def freq_palavras(frases):
    dicionario = {}
    soma = 0
    corte = str.split(frases)
    for palavra in corte:
        n = list.count(corte, palavra)
        dicionario.update({palavra:n})
    return dicionario
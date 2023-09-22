def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário
    no qual cada palavra da string seja uma chave e tenha
    como valor o número de vezes que ela aparece."""
    l = str.split(frases," ")
    d = {}
    d[e] = 1
    for e in l:
        d[e] = d[e] + 1
        d = d + d[e]
    return d
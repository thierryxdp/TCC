def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário
    no qual cada palavra da string seja uma chave e tenha
    como valor o número de vezes que ela aparece."""
    l = str.split(frases," ")
    d = {}
    dk = 1
    for e in l:
        d[e] = dk
    for i in l:
        d[i] = dk
    for e in l:
        if d[e] == d[i]:
        dk = dk + 1
    ret = d
    return ret
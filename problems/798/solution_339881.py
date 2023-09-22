def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário
    no qual cada palavra da string seja uma chave e tenha
    como valor o número de vezes que ela aparece."""
    l = str.split(frases," ")
    d = {}
    dk = 0
    for e in l:
        d = d + {e:dk}
        dk = dk + 1
    ret = d
    return ret
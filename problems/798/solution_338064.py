def freq_palavras(frases):
    l=str.split(frases)
    d = {}
    for i in l:
      n = str.count(frases, i)
      d[str(frases)]= n
    return d
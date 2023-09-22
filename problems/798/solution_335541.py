def freq_palavras(s):
    """Dado uma string s, conta quantas vezes cada palavra ocorre 
    e guarda as palavras num dicionário, cujas chave são as palvras
    e os valores de retorno o número de vezes que essa palavra o ocorre
    str-->dict"""
    a = s.split()
    i = 0
    if ',' in a:
        while i < a.count(','):
            a.remove(',')
            i = i + 1
    if '.' in a:
        while i < a.count('.'):
            a.remove('.')
            i = i + 1
    if '!' in a:
        while i < a.count('!'):
            a.remove('!')
            i = i + 1
    if '?' in a:
        while i < a.count('?'):
            a.remove('?')
            i = i + 1
    d = {a[0]:0}
    while i < len(a):
        if a[i] in d:
            d[a[i]] = d[a[i]] + 1
        if a[i] not in d:
            d[a[i]] = 1
        i = i + 1
    return d
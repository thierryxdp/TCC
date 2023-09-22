# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(s):
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
def retira_ponto(frase):
    a = str.replace(frase, '.', '')
    b = str.replace(a, ',', '')
    c = str.replace(b, ':', '')
    d = str.replace(c, ';', '')
    e = str.replace(d, '!', '')
    f = str.replace(e, '?', '')
    g = str.replace(f, '-', '')
    return g

def inverte(frase):
    nova_frase = str.lower(retira_ponto(frase))
    final = str.join(list.reverse(str.split(nova_frase, ' ')))
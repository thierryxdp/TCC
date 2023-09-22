# inverte uma frase, sem maiúsculas e sem pontação
# str -> str
def inverte(t):
    txt = t.replace('-', ' ').replace(',', '').replace(':', '').replace(';', '').replace('.', ' ').replace('!', '').replace('?', '').lower()[::-1]
    return str.join('', txt)
# inverte uma frase, sem maiúsculas e sem pontação
# str -> str
def inverte(t):
    return t.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').lower().split(' ', -1)
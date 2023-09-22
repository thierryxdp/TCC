# Dada um string s, esta função retorna uma nova string inserindo # no inicio,
# no meio e no final da string s dada.
# str-> str
def hashtag(s):
    tamanho = len(s)
    nova = '#' + s[0:tamanho//2] + '#' + s[tamanho//2:] + '#'
    return nova
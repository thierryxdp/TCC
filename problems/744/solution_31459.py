# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Calcula e retorna uma função em que o caracter "#" seja inserido no início, no meio e no fim de uma string s.
    str -> str"""
    pre = str (s) [:len(str (s))//2]
    pos = str (s) [len(str (s))//2:]
    str (s) = "#" + pre + "#" + pos + "#"
    return str (s)
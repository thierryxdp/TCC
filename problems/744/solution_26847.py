# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Dado uma string qualquer, essa funcao retorna a propria string com o caractere '#' no inicio, no meio
    e no final dela"""
    if len(s)%2==0:
        i = int(len(s)/2)
        return '#' + s[:i] + '#' + s[i:] + '#'
    else:
        p = len(s)//2
        return '#' + s[:p] + '#' + s[p:] + '#'
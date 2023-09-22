def hashtag(s):
    """Função que insere o caractere # no inicio, no meio e no final da string.
    Recebe uma string
    Retorna a string com o caractere no inicio, meio e final"""
    k = int((len(s))/2)
    return '#' + s[:k] + '#' + s[k:] + '#'
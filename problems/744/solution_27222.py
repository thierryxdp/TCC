# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Escreve # no iníco, no meio e no final da string recebida."""
    meio = len(s)//2
    return '#' + str(s[:meio])+ '#' +str(s[meio:])+ '#'
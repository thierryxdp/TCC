# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma palavra e adiciona um '#' no iníco, no meio e no final
    da palavra
    Recebe str e Retorna str"""
    i = len(s)//2
    
    return '#'+ s[0:i] + '#' + s[i:] + '#'
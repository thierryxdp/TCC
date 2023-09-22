# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string e adiciona uma hashtag no meio, no começo e no final dela"""
    
    return str('#') + s[0:len(s)//2] + str('#') + s[len(s)//2:len(s)] + str('#')
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """NNN"""
    num_carac=len(s)
    metade_carac=num_carac//2
    inicio_palavra=s[0:metade_carac]
    final_palavra=s[metade_carac:-1]
    return '#'+ inicio_palavra +'#'+ final_palavra+'#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(S:
    """esta funcao coloca # no inicio e final da string"""
    S = "#" + S[:len(S)//2] + "#" + S[len(S)//2] + "#"
    return S
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Esta funcao recebe uma string s, e a retorna com '#' no inicio, meio e
    no final."""
    if len(s)%2==0:
        metade=len(s)/2
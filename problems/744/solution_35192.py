# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao que retorna o caractere 
       no inicio, no meio e no fim 
       da string."""
    if len(s)%2==0:
        return '#'+[0:int(len(s/2))]+'#'+[int(len(s/2)):len(s)]+'#'
    else:
        return '#'+[0:int(len(s/2))]+'#'+[int(len(s/2):len(s))]+'#'
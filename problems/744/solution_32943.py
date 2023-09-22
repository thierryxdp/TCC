# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ' Essa função faz modificações no início, final e no meio da string. '
    # cria espaços
    i=0
    if (len(string))%2==0:
        i=int(len(string)/2)
    else:
        i=int((len(string)-1)/2)
    resultado= '#'+string[0:i]+'#'+string[i:]+'#'
    return resultado
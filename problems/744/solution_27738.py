# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    lista = list(s)
    tam = len(s)

    i = int((tam/2))
    s= s+'#'
    s= '#'+s

    if tam==0:
        return s
    elif tam==1:
        lista[s+'#']+lista['#'+s]
    else:
        x = lista [i]
        lista [i]=s
        lista [i+1]= (x+lista[i+1])


    s = ''.join(lista)
    return s
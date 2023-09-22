# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    inicio = 0
    meio = int((len(s)/2))+1
    slist = list (s)
    slist.insert (inicio,'#')
    slist.insert (meio,'#')
    slist.append ('#')
    resultado = slist
    return resultado
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s1= int(len(s)/2)
    s2= len(s)/2
    if(int!=len(s)/2):
        return '#'+ s[0:s1] + '#' + s[s1:]+'#'
    else:
        return '#'+ s[0:s2]+'#'+s[s2:]+'#'
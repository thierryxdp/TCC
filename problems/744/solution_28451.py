# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(str(s))%2==0:
        return '#'+ str(s)[0:len(str(s))//2]+ '#'+ str(s)[len(str(s))//2+1:] + '#'
    else:
        return '#'+ str(s)[0:len(str(s))//2+1]+'#'+str(s)[len(str(s)):]+'#'
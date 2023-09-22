# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    if len(s)==4:
        return '#'+ s[:2]+ '#'+ s[2:]+ '#'
    elif len(s)==5:
        return '#' + s[:3]+ '#'+ s[3:] +'#'
    elif len(s)>=6:
        return '#'+ s[:3]+ '#'+ s[3:] + '#'
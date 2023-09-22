# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' retorna uma string com hashtaga no início, no meio e no final. dada a string s; str -> str''' 
    t=len(s)/2
    v=(len(s)-1)/2
    w=(len(s)-1)/2
    if t==0:
        return('#'+s[:t]+'#'+s[t:]+'#')
    else:
        return('#'+s[:v]+'#'+s[w:]+'#')
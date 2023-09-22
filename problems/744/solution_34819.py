# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' retorna uma string com hashtaga no início, no meio e no final. dada a string s; str -> str''' 
    t=len(s)
    if t%2==0:
        return('#'+s[:t/2]+'#'+s[t/2:]+'#')
    else:
        return('#'+s[:(t-1)/2]+'#'+s[(t+1)/2:]+'#')
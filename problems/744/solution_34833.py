# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' retorna uma string com hashtaga no início, no meio e no final. dada a string s; str -> str''' 
    return('#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#')
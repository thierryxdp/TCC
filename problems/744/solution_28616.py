"""recebe uma string e insere hashtags em seu inicio, meio e fim
s->string
str-> str"""
def hashtag(s):
    return str(#)+s[0:len(s)//2]+str(#)+s[len(s)//2:]+str(#)
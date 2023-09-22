# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ asas"""
    partir= len(s)
    priparte= s[0:i]
    seqparte= s[i+1:]
    
    if (i)==0:
        return x + s[1:]
    else:
        return priparte+x+seqparte
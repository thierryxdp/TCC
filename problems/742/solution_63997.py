# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ asas"""
    parte= len(s)//i
    priparte= s[0:1+parte]
    seqparte= s[parte+2:]
    if i==0:
        return (s)
    else:
        return priparte+x+seqparte
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ asas"""
    metade= len(s)//2
    comeco= s[0:metade]
    fim= s[metade:]
    return '#' + comeco +'#'+ fim + '#'
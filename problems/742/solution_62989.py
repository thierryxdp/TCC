# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """a partir da string inicial um valor de uma posição e outra string, a função subistitui a string enviada pelo
    caractere na posição desejada"""
    antes = s[0:i]
    dps = s[i+1:]
    return antes+x+dps
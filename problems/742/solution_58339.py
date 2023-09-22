# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Parametros:
    Entrada:
    s=string
    x=string
    i=inteiro entre 0 e comprimento da string 's' """
    y=s[i]
    resposta=s[0:i]+s[i:-1]
    return resposta
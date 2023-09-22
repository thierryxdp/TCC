# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ função que substitui um caractere qualquer
    em uma posição da string fornecida.
    assinatura: str,str,int --> str
    """
    return s[0:i]+ x + s[i+1:(-1)]
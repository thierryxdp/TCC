# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que substitui o carectere de número "i" da string "s" pelo
    caractere "x" e retorna a string resultante desse processo"""
    p1=s[:i]
    p2=s[-1:i:-1]
    p2=p2[::-1]
    return p1+x+p2
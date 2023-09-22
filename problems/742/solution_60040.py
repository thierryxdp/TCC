# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe duas strings e subistuí um caracter pelo número
    de entrada str,str,int -> str
    Use s: String
    Use x: Caracter que substituirá
    Use i: Inteiro entre 0 e o comprimento da String"""
    s = list(s)
    s[i] = x
    nova_string = ''.join(s)
    return nova_string
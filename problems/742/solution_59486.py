# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """essa função irá substituir uma caractere x de uma string s na posição i que pode ser de 0 ate a ultima letra da string
    string, int, int -> string"""
    return s[0:i]+x+s[i:]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função recebe um string (s) e substitui o caractere na posição i (int entre 0 e o comprimento da string) por
    x, retornando a string com a substituição,
    string, int, int -> string"""
    
    s=s[:i]+str(x)+s[i+1:]
    return s
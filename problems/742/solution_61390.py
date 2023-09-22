# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que substitui o caractere na posicao i de um string s, por um caractere x
    parametros: s,x,i -> str, str, int
    retorna: str"""
    s[0:i] + s[i+1:]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que ao dar como entrada uma string, um caractere x (uma substring) e um numero inteiro i entre 0 e o comprimento da string, retorna a string mas com o elemento da posicao i substituido pelo caractere. parametros: str,str,int --> str."""
    return str.replace(s,s[i],x)
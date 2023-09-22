# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma strin s, um caracter x e um número inteiro i 
    entre 0 e o comprimento da string, e retorna uma string igual a s:
     srt,srt,int -> str"""
    return s[0:i] + x + s[i+1:len(s)]
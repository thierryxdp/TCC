# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """dado uma string, um caractere e um numero n de valor menor ou igual o tamanho da string, retorna a string com a substituicao do n'esimo termo pelo caratere dado;
    str, str, int -> str"""
    if i==0:
        return x+s[1:len(s)]
    else:
        return s[0:i]+x+s[i+1:len(s)]
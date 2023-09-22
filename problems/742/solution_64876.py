# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''muda o caracter de posição i, de uma string s, pelo caracter x dado
       str, str, int -> str'''
    Caracteres= len(s)
    j=i+1
    return str(s[0:i])+str(x)+str(s[j:Caracteres])
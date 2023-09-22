# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''s=str,x=caractere,i=int entre o e len(s).
srt,int,int->str'''
    return s[0:i-1]+x+s[i:]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s=list(s)
    s[i]=x
    
    return ''.join(s)
#A função transforma a string 's' numa lista, substitui o 
#elemento [i] da lista pelo caracter 'x', 
#e depois transforma e retorna a lista
#modificada numa string novamente.
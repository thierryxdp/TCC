# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao recebe uma str s,caractere x e um numero int i entre 0 e 
    o comprimento da str igual a s,elemento i substituido poor x
    ent->str,int
    saida->str,int
    """
def substitui(s,x,i):
    f=s[0:i]
    f=f+str(x)
    return f+s[i+1:]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """recebe uma string s, com um caractere x e um numero inteiro i entre 0 e o 
       comprimento da string, e retorna uma string igual a s, exceto que o elemento 
       da posição i deve ser substituido pelo caractere x;
       assinatura: string, int, int--.string
       teste:
       """
l=list(s)
l[i]=x
s="".join(1)
    return s
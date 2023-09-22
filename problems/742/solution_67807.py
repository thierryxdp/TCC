# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string s, um caractere x e um
    número inteiro i entre 0 e o comprimento da string, e 
    retorne uma string igual a s, exceto que o elemento da
    posição i deve ser substituído pelo caractere x.
    string,int,int -> string"""
    l=len(s)
    if 0<=i<=l:
        r=list(s)
        r[i]=str(x)
        s="".join(r)
        return s
    if i>l:
        return " "
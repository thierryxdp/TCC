# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'dada uma string(s),a posicao da letra que quer mudar(i) e o caractere que quer incluir(x),retorna uma nova string alterada'
    'string,string,int->string'
     S=s
    L=list(S)
    L[i]=x
    S="".join(L)
    return S
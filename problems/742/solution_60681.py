# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    tam=len(s)
    l=s[i] #define a letra na posição i
    if tam>i:
        letra=str.partition(s,l) #separa a palavra em três partes, antes de l e depois de l 
        s1=letra[1]
        s3=letra[3]
        return s1+x+s3
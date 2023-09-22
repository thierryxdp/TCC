# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    tam=len(s)
    l2=s[i] #define a letra na posição i
    if tam>i:
        letra=str.partition(s,s[i]) #separa a palavra em três partes, antes de l2 e depois de l2 em uma lista com 3 pos 
        s1=letra[0] #primeira parte da string antes de l2(posição 0 de letra)
        s3=letra[2] #segunda parte da string depois de l2(posição 2 de letra)
        return s1+x+s3 #soma a primeira parte+x+segunda parte, concluindo a substituição.
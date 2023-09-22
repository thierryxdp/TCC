# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    a=list
	s=list(s)
    s[i+1]=x
    for z in range(0,len(s)):
        a.append(s[z])
    return(a)
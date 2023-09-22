# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i>(len(s)-1) or i<-len(s):
        return "o número escolhido deve estar entre "+str(-len(s))+" e "+str(len(s)-1)

    else:
        return s.replace(s[i],x)
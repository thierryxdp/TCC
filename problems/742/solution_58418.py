# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que substitui a letra escolhida por um determinado caractere """
    if i>(len(s)-1) or i<-len(s):
        return "o número escolhido deve estar entre "+str(-len(s))+" e "+str(len(s)-1)
            
        
    elif len(s) == 1:
        return s.replace(s[0],x)
    elif i==(len(s)-1)or i==(len(s)-2):
        return s.replace(s[i-2:i+1],s[i-2]+s[i-1]+x)
    else:
        return s.replace(s[i:i+3],x+s[i+1]+s[i+2])
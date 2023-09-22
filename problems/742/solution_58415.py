# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i>(len(s)-1) or i<-len(s):
        return "o número escolhido deve estar entre "+str(-len(s))+" e "+str(len(s)-1)
    elif i==(len(s)-1):
        return s.replace(s[i-1:i+1],s[i-1]+x)        
        
    
    else:
        #return s.replace(s[i],x)
        return s.replace(s[i:i+2],x+s[i+1])
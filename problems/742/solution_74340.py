# Substitui um caractere de uma string
# conta =  verifica quantos caracteres há em uma string e aux, aux1 e aux2 = sao 
# variaveis auxiliares para fatiarem a string
# string, string, int -> string
def substitui(s,x,i):
    conta= len(s)        
    if i>=1:
        aux1= s[0:i]
        aux2=s[i+1:conta]
        return str(aux1)+str(x)+str(aux2)
    else:
        aux=s[i+1:conta]
        return str(x)+str(aux)
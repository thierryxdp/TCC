#Função que recebe uma strnig s, um caractere x e um numero nteiro i entre 0 e o comprimento da string, 
#e retorne uma string igual a s
# string,string, int -> string
def substitui(s,x,i):
    primeiro=s[0:i]
    segundo=s[i+1:len(s)]
    return primeiro+x+segundo
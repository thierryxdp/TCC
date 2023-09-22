#Função que substitui em uma string s, um caractere x num número inteiro i
#Retornando a string mas com o caractere na posição i
# string, int, int -> string
def substitui(s,x,i):
    primeiro = s[:i]
    segundo = s[i+1:]
    return segundo
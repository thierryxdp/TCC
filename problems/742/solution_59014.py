# Retorna uma nova string a partir da modificação da que entrou
#s=string,x=caractere que irá repor,i=número inteiro
# string, int, int -> string
def substitui(s,x,i):
    novastr=s[:i]+x+s[i+1:]
    return novastr
def substitui(s, x, i):
    #Entrada, dos três parâmetros, respectivamente,
    #definido por string, x e um número inteiro, o i, que fique
    #no zero de acordo com o comprimento da string
    #retornando uma string igual a s, contudo o i não pode ser x
    #string, int, int -> string
    if i==0:
        return x+s[1:]
    
    else: 
        return x+s[1:]
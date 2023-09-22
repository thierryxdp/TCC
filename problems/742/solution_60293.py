def substitui(s,x,i):
    #Dados os seguintes inputs string(s), caractere(x) e posição(i), retorne a string s substituindo o elemento na posição i pelo caractere x
    #string, string, int -> string
    return s[0:i] + str(x) + s[(i+1):]
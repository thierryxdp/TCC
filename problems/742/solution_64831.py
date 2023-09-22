def substitui(s,x,i):
    " Substitui uma letra na determinada posição escohida" 
    #str, str, int -> string"
    Parte1 = s[0:i]
    Parte2 = s[i+1:len(s)]
    return Parte1+x+Parte2
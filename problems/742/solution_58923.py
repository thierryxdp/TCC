def substitui(s,x,i):
   #Essa função recebe uma string, um caractere e um numero intreiro i entre 0 e o comprimento da string, retornando uma string igual a inserida, exceto que o elemento da posição i deve ser substituido pelo caractere x
   #str,str,int -> str
    s = s[:i] + x + s[i+1:]
    return s
# string, int, int -> string
def substitui(s,x,i):
    #repete as letras antes e depois do termo na posição i e coloca o caractere x entre as partes
    return s[0:i]+str(x)+s[i+1:]
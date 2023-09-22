# Essa função substitui o caracter desejado na string dada 
# pela letra 's', por um caracter qualquer 'x' na posição 'i'
# onde 'i' é menor que a quantidade de caracteres de 's'. 
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i]+str(x)+s[i+1:len(s)]
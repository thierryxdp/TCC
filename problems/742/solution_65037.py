"""apartir da string obtida, e selecionado um caracter para substiuir 
	o valor do caracter representado na string, apenas indicando o numero
    representado que ele encaixa na string"""
# string, int, int -> string
def substitui(s,x,i):
    return str(s[:i]+str(x)+s[i+1:])
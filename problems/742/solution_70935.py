def substitui(s,x,i):
#Função que substitui um caractere em uma certa posição
#especificada e retorna a nova string com o caractere
#substituido.
# string, int, int -> string
    #if i < 0 or i > len(s)
    	#return "A string é maior ou menor que o index solicitado."
    #else:
    newstr = s[0:i] + x + s[i+1:len(s)-1]
    return newstr
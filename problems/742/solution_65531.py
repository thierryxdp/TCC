#Ira receber uma string, um caractere x e um numero inteiro i entre o , retornar uma uma string igual a s.Com exeçao os elementos da posiçao i deve ser substituido pelo x
#s,x,i
# string, int, int -> string
def substitui(s,x,i):
    """Funçao que recebera uma strin s, uma aracter x e um numero inteiro i entre  e o copriento string, e retornara uma string igual a s, exceto o elemento da posicao i deve ser substituido pelo x"""
    s[i]= x
    return s
#return s [0:i] + x +s [i+1:]
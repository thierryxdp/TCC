# Escreva uma fun¸c˜ao que receba uma string s, um caractere x e um n´umero
# inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s,
# exceto que o elemento da posi¸c˜ao i deve ser substitu´ıdo pelo caractere x.
# string, int, int -> string

def substitui(str1, x, i):
    str1[i] = x
              
    return str1
   # return str1[0:i] + x + str1[i + 1:]
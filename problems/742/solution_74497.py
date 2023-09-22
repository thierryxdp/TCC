# Escreva uma funcao que receba uma string s, um caractere x e um numero
# inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s,
# exceto que o elemento da posicao i deve ser substituıdo pelo caractere x.

def text_char(str1, x, i):
    str1[i] = x
    return str1
  # return str1[0:i] + x + str1[i + 1:]
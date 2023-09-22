def substitui(s,x,i):
    """ A Função irá substituir a string s, o caractere x e um número inteiro i entre 0 e o comprimento
    da string, e tirá retornar uma string igual a s, substituindo o elemento i pelo caractere x. """
    substitui = s[0:posicao] + x + s[posicao+1:len(s)]
    return substitui
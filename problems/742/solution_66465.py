#Questao 2
def substitui(t ,x, i):
    '''
Funcao que recebe uma string s, um caractere x e
um numero inteiro i entre 0 e o comprimento da string,
e retorne uma string igual a s, exceto o elemento da posicao
i que deverá ser trocado por x.
return s[0:i] + x + s[i+1:]
   '''
    s[i] = x
    return s
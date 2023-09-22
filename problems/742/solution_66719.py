def substitui(s,x,i):
    '''calcule  uma função que recaba uma string 's', um caractere 'x' e um número inteiro 'i' entre zero e o comprimento da string, e retorne uma string igual a 's', exceto que o elemento da posição 'i' deve ser substituído pelo caractere 'x'. str, str,int-->str.'''
    funcao = s((0:i)) + x 
    if s((i)) == s((-1)) and (i + 1) != len (s):
        return funcao + s(((1+i):-1)) + s((-1))
    elif s((i)) == s((-1)):
        return funcao
    elif s((i)) != s((-1)):
        return funcao + s(((i+1):-1)) + s((-1))
def substitui(s,x,i):
    """ Dados uma string 's', um caractere 'x' e um numero inteiro 'i' 
        entre 0 e o comprimento da string, retornando uma string igual a 
        string 's' substituindo o elemento da posicao 'i' pelo 
        caractere x. """
    stringNova = s[0:i] + x + s[i+1:len(s)]
    return stringNova
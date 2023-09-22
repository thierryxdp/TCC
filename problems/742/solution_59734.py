def substitui(s,x,i):
    """ Dados uma string 's', um caractere 'x' e um numero inteiro 'i' 
        entre 0 e o comprimento da string, retornando uma string igual a 
        string 's' substituindo o elemento da posicao 'i' pelo 
        caractere x. """
    stringNova = string[0:posicao] + caractere + string[posicao+1:len(string)]
    return stringNova
def substitui(s,x,i):
    ''' Função que recebe uma string 's', um caractere 'x' e um número inteiro 'i' entre 0 e o comprimento da string e retorna uma string igual a s,
    substituido o elemento da posição i por x. string, int, int -> string '''
    string = s
    string = string[:i] + x + string[i+1:]
    return string
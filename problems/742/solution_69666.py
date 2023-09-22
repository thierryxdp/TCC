def substitui(s,x,i):
    '''Função que receba uma strig s, um caractere x e um número inteiro i entre 0 e o comprimento da string,e reorn uma string igual a s, exeto que o elemento da posição i deve ser substituído pelo caractere x'''
    if len(s,x):
        return [str(s)+'#'+(i[0:])]
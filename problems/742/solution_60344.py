def substitui(s,x,i):
    '''Função que, dado uma string(s), um caractere (x) e um número inteiro (i) entre 0 e o comprimento da string, retorna uma string igual a string dada como entrada, porém com o elemento da posição i substituído pelo caractere x; str, int, int -> str.'''
    if (i >= 0 and i <= len(s):
        s1 = s[:i]
        s2 = s[i:]
        return s1 + str(x) + s2
def substitui(s, x, i):
    '''Retorna uma string igual a s, substituindo o caractere
       da posiçao i pelo caractere x.
       str, str, int -> str'''
    string1 = s[:i]
    string2 = s[i+1:]
    return string1+x+string2
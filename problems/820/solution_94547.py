def posLetra(s,l,n):
    '''retorna a posição em que a enésima repetição de l está em uma frase s
    string, string, int -> int'''
    cont = 0
    ocor = 1
    a = str.count(s,l)
    if a < n:
        return -1
    else:
        b = s[cont]
        while ocor < n:
            if b == l:
                ocor = ocor + 1
            cont = cont + 1
        return cont
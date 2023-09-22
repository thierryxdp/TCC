def posLetra(s,l,n):
    '''retorna a posição em que a enésima repetição de l está em uma frase s
    string, string, int -> int'''
    a = str.count(s,l)
    if a < n:
        return -1
    else:
        cont = 0
        ocor = 0
        y = n
        while ocor < y:
            b = s[cont]
            if b == l:
                ocor = ocor + 1
            cont = cont + 1
        return (cont-1)
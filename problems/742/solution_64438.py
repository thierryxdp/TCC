def substitui(s,x,i):
    """string 's' um caractere 'x' e um int 'i'
    return string igual a s exeto o elemento da posição i, substituida
    caractere x
    str-->str"""

    return s[0:i]+(x) + s[i+1:]
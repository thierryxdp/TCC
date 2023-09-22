def substitui(s ,x , i):
    """Recebe uma string, um caractere x e um numero entre 0 e o comprimento de string e substitui esse caractere em uma determinada posição da string. str + int + str -> str"""
    a = list(s)
    a[i] = x
    return str.join("",a)
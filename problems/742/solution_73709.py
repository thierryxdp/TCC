def substitui(s,x,i):
    """Recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string e retorna uma string igual a s, exceto pelo o elemento i que substitui o caractere x
    str + int + str -> str"""
    a = list(s)
    a[i] = x
    return str.join a
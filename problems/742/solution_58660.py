def substitui(s,x,i):
    '''Calcula e retorna uma string diferente da inicial ao alterar um elemento qualquer por outro em uma determinada posiçao
    str, int, int -> str
    parameters:
    s: string qualquer a ser utilizada
    i: posiçao de troca entre caracteres
    x: caracter qualuqer a ser colocado'''
    return s[0:i] + 'x' + s[i+1:]
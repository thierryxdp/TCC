def substitui(s,x,i):
    '''Dados uma string, um caractere e um inteiro, retorna uma string substituindo o caractere de índice i por x
    str, int, int -> str'''
    if i >= 0 and i < len(s):
        return s[:i] + x + s[(i + 1):]
    else:
        return "não correspondente a nenhum caractere da string"
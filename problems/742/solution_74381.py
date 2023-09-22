def substitui(s,x,i):
    """Esta função recebe uma string, um determinado caractere e um numero inteiro na mesma
    string, mas na mesma posição do numero inteiro recebido.
    assinatura: str, str, int -> str
    testes:
    substitui('passei', 'z', 3)='paszei'
    substitui('serrar', 'c', 0)='cerrar'
    substitui('sim', 'o', 1)='som'
    """
    return s[0:i]+x+s[i+1:]
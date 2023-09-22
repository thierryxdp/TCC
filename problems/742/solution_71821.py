def substitui(s, x, i):
    '''Esta função recebe uma string, um determinado caractere e um número inteiro, e retorna a
    mesma string, porém, na posição do número inteiro recebido, substitui um caractere pelo desejado
    assinatura: str, str, int -> str
    testes:
    substitui('passei','z',3)='paszei'
    substitui('serrar','c',0)='cerrar'
    substitui('sim','o',1)='som'
    '''
    return s[0:i] + x + s[i + 1:]
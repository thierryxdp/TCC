# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    Essa função recebe uma string 's', um número inteiro i, tal que
    0 <= i <= len(s), e retorna uma string igual a s, sendo s[i] = x.
    """
    str_resultado = ''
    for indice, letra in enumerate(s):
        if indice == i:
            str_resultado += x
        str_resultado += letra
    return str_resultado
def substitui(s,x,i):
    '''Função que substitui determinado caractere de uma string por outro
    caracter. As entradas são: s (string), x (novo caractere) e i (posição
    do caractere que vai ser trocado).
    OBS: o 'i' deve estar entre 0 e o comprimento da string.
    str, float, int -> str'''
    novaString = s[:i]+x+s[i+1:]
    return novaString
def conta_frases(texto):
    """
    Essa função recebe uma string (texto) e retorna quantas frases 
    têm nesse texto;
    str -> int
    """
    ponto_final = '.'
    exclamacao = '!'
    interrogacao = '?'
    reticencias = '...'
    str1 = ''
    lista = []
    proximo = 0
    while proximo < len(texto):
        for v in texto:
            str1 += v
            texto = texto.replace(v, '')
            proximo += 1
            if v == ponto_final or v == exclamacao or v == reticencias or v == interrogacao:
                lista += [str1]
                str1 = ''
                continue
        lista += [texto]
    return len(lista)
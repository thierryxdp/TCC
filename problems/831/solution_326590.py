def lingua_p(palavra):
    """Recebe uma palavra em português e retorna a mesma palavra na língua do p.
    str -> str"""
    str.lower(palavra)
    palavra_p = ''
    lista_palavra = list(palavra)
    for i in lista_palavra:
        if i in 'aáàãäâeéèêëiíìîïoóòõôöuúùûü':
            palavra_p += i + 'p' + i
        else:
            palavra_p += i
    return palavra_p
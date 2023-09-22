def lingua_p(palavra):
    '''retorna a palavra fornecida traduzida para a lingua do p,
    em minuscula; str -> str'''
    traduzida=''
    i=0
    while i<len(palavra):
        if palavra[i]in'aeiouAEIOU':
            traduzida=palavra[:i+1]+'p'+palavra[i]+palavra[i:]
        i=i+1
    return str.lower(traduzida)
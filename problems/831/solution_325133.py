def lingua_p(palavra):
    """Recebe uma palavra em português e retorna essa palavra
    na lingua do P, com todas as letras em minúsculas
    str->str"""
    pal_min=str.lower(palavra)
    vogais='aàáãâeéêiíoóõôuú'
    str_traduzida=''
    for i in range(len(pal_min)):
        if pal_min[i] in vogais:
            str_traduzida += pal_min[i]+'p'
        str_traduzida += pal_min[i]
    return str_traduzida
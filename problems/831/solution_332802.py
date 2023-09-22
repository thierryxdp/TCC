def lingua_p(palavra):
    """Função que retorna uma palavra traduzida para a língua p; str->str"""
    convertido=""
    palavras=str.lower(palavra)
    for letra in palavras:
        if letra in 'aeiouãõéíóáúêâô':
            convertido+=letra+'p'+letra
        else:
            convertido+=letra
    return convertido
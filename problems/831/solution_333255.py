def lingua_p(palavra):
    """Retorna uma palavra em portugues passada
    como parametro, traduzida para a lingua do p.
    str -> str"""
    vogais = 'aeiouãõáéíóúàèìòù'
    linguap = ''
    for i in palavra.lower():
        if i not in vogais:
            linguap += i
        else:
            linguap += i + 'p' + i
    return linguap
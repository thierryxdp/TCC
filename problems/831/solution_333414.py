def lingua_p(palavra_portugues):
    traduzindo_p=[]
    contador=0
    for letra in list(palavra_portugues):
        if str.lower(letra) in 'aeiouáéíóúâêîôûãẽĩõũ':
            traduzindo_p.append(letra+'p'+letra)
        else:
            traduzindo_p.append(letra)
    return ''.join(traduzindo_p)
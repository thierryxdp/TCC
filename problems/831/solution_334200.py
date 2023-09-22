def lingua_p(palavra):
    traducao=[]
    frase=str.lower(palavra)
    for letra in frase:
        if letra in 'aeiouáéíóúâêîôûàèìòùãõ':
            traducao.append(letra+'p'+letra)
        else:
            traducao.append(letra)
    return ''.join(traducao)
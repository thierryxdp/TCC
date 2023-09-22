def lingua_p(palavra):
    traducao=[]
    frase=str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            frase.append(letra+'p'+letra)
        else:
            frase.append(letra)
    return ''.join(frase)
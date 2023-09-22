def lingua_p(frase):
    frase1=str.lower(frase)
    soma=''
    for i in range(len(frase1)):
        if frase1[i] in 'aeiouáéíóúâêîôãõ':
            soma=soma+frase[i]+'p'+frase[i]
        else:
            soma=soma+frase1[i]
    return soma
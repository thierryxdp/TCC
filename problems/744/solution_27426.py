def hashtag(frase):   
    total = 0
    for i in frase:
        total = total + 1
    if (total % 2) == 0:
        x = (total/2)
        primeira_metade = frase[:int(x)]
        segunda_metade = frase[int(x):]
        hasht = "#"
        resultado = hasht + primeira_metade + hasht + segunda_metade + hasht
        return resultado
    else:   
        x = (total/2)
        y = (total/2)
        primeira_metade = frase[:int(x)]
        segunda_metade = frase[int(y):]
        hasht = "#"
        resultado = hasht + primeira_metade + hasht + segunda_metade + hasht
        return resultado
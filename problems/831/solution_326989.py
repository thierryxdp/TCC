def lingua_p(frase):
    for index in range(frase):
        if index=='AEIOUaeiou':
            resultadoP=frase[:index]+ 'p' + frase[index+1]
        else:
            pass
    return resultadoP
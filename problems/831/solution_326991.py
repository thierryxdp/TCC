def lingua_p(frase):
    fraseList=list(frase)
    for index in frase:
        if index=='AEIOUaeiou':
            resultadoP=frase[:index]+ 'p' + frase[index+1]
        else:
            pass
    return resultadoP
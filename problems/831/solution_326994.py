def lingua_p(frase):
    fraseList=list(frase)
    resultadoP=''
    for index in frase:
        if frase[index] in 'AEIOUaeiou':
            resultadoP=frase[:index]+ 'p' + frase[index+1]
        else:
            pass
    return resultadoP
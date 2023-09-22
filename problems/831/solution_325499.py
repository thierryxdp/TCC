def lingua_p(frase):
    resultado=''
    for palavra in frase:
        if palavra not in 'AEIOUaeiou':
            x=str.lower(palavra)
            resultado=resultado+x
        if palavra in 'AEIOUaeiou':
            x=str.lower(palavra)
            resultado=resultado+ x+str('p')
    return resultado
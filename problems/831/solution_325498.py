def lingua_p(frase):
    
    resultado=0
    for palavra in frase:
        if palavra in 'AEIOUaeiou':
            x=str.lower(palavra)
            resultado= x+str('p')+palavra
    return resultado
lingua_p('cabeça')
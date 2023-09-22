def lingua_p(palavra):
    texto = ''
    palavra.lower()
    for i in range(len(palavra)):
        if 'i' in 'aeiou':
            texto+= 'i'+'p'+'i'
        else:
            texto+= 'i'
            
    return texto
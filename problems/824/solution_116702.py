def uppCons(frase):
    i=0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouáéíóúãõàèìòù':
            str.upper(frase,frase[i])
        i=i+1
        return frase
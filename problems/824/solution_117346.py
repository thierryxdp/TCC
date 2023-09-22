def uppCons(frase):
    i=0
    texto=''
    while i< len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            texto= texto+frase[i].upper()
            i=i+1
    return texto
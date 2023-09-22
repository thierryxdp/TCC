def uppCons(frase):
    '''dada uma frase em string, é retornado a mesma frase,
	porem com as suas consoantes agora em letra maiuscula
    str-->str'''
    novaFrase=''
    i=0
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãÂ':
            novaFrase=novaFrase+str.upper(frase[i])
        if frase[i] in 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãÂ':
            novaFrase=novaFrase+frase[i]
        i=i+1
    return novaFrase
def posLetra(frase,letra,ocorrencia):
    '''Recebe uma frase, uma letra e um número inteiro indicando a ocorrência, 
       retorna a posição da frase em que aquela ocorrência da letra se encontra.
       str, str, int->int
       
       Parameters:
       frase: A frase que sera usada como base da função.
       letra: A letra que sera procurada dentro da frase.
       ocorrencia: Indica qual ocorrência da letra na função deve procurar.'''
    if frase.count(letra)<ocorrencia:
        return -1
    else:
        i=0
        letras=[]
        caracteres=list(frase)
        while i<len(caracteres)and len(letras)<ocorrencia:
            if letra==caracteres[i]:
                list.append(letras,caracteres[i])
            i=i+1
        return i-1
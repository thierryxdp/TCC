def posLetra(frase,letra,ocorrencia):
    '''
       Dada uma frase, uma letra e a a ocorrencia da letra 
       desejada função retorna a posição que a letra 
       se encontra no número de ocorrência desejada, caso o
       número de ocorreência pedida seja maior que a 
       ocorrência da letra na frase o retorno é -1.
       str, str, int -> int
    '''
    if frase.count(letra)<ocorrencia:
        return -1
    else:
        i=0
        letras=[]
        caracteres=list(frase)
        while i<len(caracteres) and len(letras)<ocorrencia:
            if letra == caracteres[i]:
                list.append(letras,caracteres[i])
            i=i+1
        return i-1
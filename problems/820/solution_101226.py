def posletra(frase,letra,ocorrencia):
    '''função que retorna a posição na string em que a ocorrencia desejada,z, de letra,y, se encontra na frase,x,retornando menos 1 caso não haja ocorrência da letra'''
     i = 0
        letras = []
        caracteres = list(frase)
    if carecteres.count('letra')<ocorrencia:
        return -1
    else:
        while i < len(caracteres) and len(letras) < ocorrencia:
            if letra == caracteres[i]:
                list.append(letras, caracteres[i])
            i = i + 1
        return i - 1
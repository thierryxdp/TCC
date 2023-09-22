def lingua_p(palavra):
    i=0
    texto_retorno = ''
     for i in range(0,len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
           texto_retorno += str.upper(palavra[i])
        else:
           texto_retorno += 'p'+ palavra[i]
        i=i+1
    return texto_retorno
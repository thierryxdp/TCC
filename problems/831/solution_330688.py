def lingua_p(palavra):
    i=0
    texto_retorno = ''
     for i in range(0,len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
           texto_retorno += 'p'+ palavra[i]
        else:
           texto_retorno +=  palavra[i]
    return str.lower(texto_retorno)
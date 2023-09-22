def Lingua_p(palavra):
    somaStr=''
    for i in range(len(palavra)):
        if palavra[i] in 'aAáÁàÀãÃeEéÉiIíÍoOóÓôÔuUúÚ':
            somaStr=somaStr+palavra[i]+p+palavra[i]
        if palavra[i] not in 'aAáÁàÀãÃeEéÉiIíÍoOóÓôÔuUúÚ':
            somaStr=somaStr+palavra[i]
    return somaStr
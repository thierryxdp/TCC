def lingua_p(palavra):
    '''recebe como parametro uma palavra (em portugues) e retorna esta mesma palavra
traduzida para a lıngua do P. Uma palavra foi traduzida para a ĺıngua do P quando, apos cada vogal da palavra original,
́e inserida a sequencia de letras p mais a vogal original.'''
    i=0
    texto_retorno = ''
    for i in range(0,len(palavra)):
        if palavra[i] in 'aeiouAEIOUáéíóúÁÉÍÚÓ':
           texto_retorno += palavra[i]+'p'+ palavra[i]
        else:
           texto_retorno +=  palavra[i]
    return str.lower(texto_retorno)
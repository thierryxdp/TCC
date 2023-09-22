def lingua_p(palavra):
    '''função que dada uma palavra, retorna uma string com essa palvra com a adiçao
       do 'p' junto com a vogal que o precede a cada vogal. str -> str'''
    acumulador = ''
    for i in palavra:
        if i in 'aeiouAEIOUÁáÉéÍíÓóÚú':
            acumulador = acumulador + i + 'p' + i
        else:
            acumulador = acumulador + i
    return acumulador
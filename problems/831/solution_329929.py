def lingua_p(frase):
    '''
       Funcao que traduz uma frase na lingua portuguesa para a lingua o P.
       str -> str
    '''
    nova_frase = ''
    for elem in range(0,len(frase)):
        if frase[elem] in 'aeiouAEIOU':
            return nova_frase = nova_frase +  str.replace(frase,str(frase[elem]),str(frase[elem]) + 'p' + str(frase[elem])
def conta_frases(texto):
'''
inicialmente vi um entrave para apenas usar a função split, visto que se o texto tiver "...",
a função não vai saber distinguir as reticências do ponto final.
Por isso, criei esta condicional e usei a função split.
'''
    if str.count(texto,"...") == 0:
        '''
        Se não há reticências, não há a necessidade de criar um linha pra as reticências.
        '''
        pts = str.split(texto,".")
        n_pts = len(pts) - 1
        '''
        pts é a lista das frases terminada em pontos separadas menos 1, pois essa é um termo repetido.
        '''
        exc = str.split(texto,"!")
        n_exc = len(exc) - 1
        '''
        exc é a lista das frases terminada em exclamação separadas menos 1, pois essa é um termo repetido.
        '''
        ite = str.split(texto,"?")
        n_ite = len(ite) - 1
        '''
        ite é a lista das frases terminada em interrogações separadas menos 1, pois essa é um termo repetido.
        '''
        frases = n_pts + n_exc + n_ite + n_ret
        ''' 
        frases é o numero de frases que foi contada com o uso do método len para as três listas acima.
        '''
        return frases
    '''
    retorna string -> int
    '''
    else:
        '''
        Aqui entra caso o texto possua as reticências
        '''
        a = str.count(texto,"...")
		'''
        Conta o número de Reticências to Texto
        '''
        ret = str.split(texto,"...")
        n_ret = len(ret) - 1
        '''
        Separa o texto na reticência e cria a lista com as frases separadas menos 1, que é uma repetida.
        '''
        pts = str.split(texto,".")
        n_pts = len(pts) - 3*a-1
        '''
        Essa é a mais problemática, visto que a função não distingue a reticências dos pontos, então ela separa 3 vezes a frase para cada reticência.
        Sabendo disso, peguei o valor a, que é o número de vezes que as reticências aparece e multipliquei por 3, visto que o split vai separar 3 vezes para cada reticências
        e subtrai 1, que é um valor repetido.
        '''
        exc = str.split(texto,"!")
        n_exc = len(exc) - 1
        '''
        Faz a mesma coisa que na condição anterior
        '''
        ite = str.split(texto,"?")
        n_ite = len(ite) - 1
        '''
        Faz a mesma coisa que na condição anterior
        '''
        frases = n_pts + n_exc + n_ite + n_ret
        '''
        Faz a mesma coisa que na condição anterior
        '''
        return frases
    '''
    Retorna string -> int
    '''
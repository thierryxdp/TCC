def retira_pontuacao(texto):
    trav = str.split(texto,"-")
    texto1 = " ".join(trav)
    '''
    O Primeiro retira os travessões e o segundo converte a lista formada em string novamente
    '''
    virg = str.split(texto1,",")
    texto2 = " ".join(virg)
    '''
    O Primeiro retira as vírgulas e o segundo converte a lista formada em string novamente
    '''
    dois_pts = str.split(texto2,",")
    texto3 = " ".join(dois_pts)
    '''
    O Primeiro retira os dois pontos e o segundo converte a lista formada em string novamente
    '''
    pts_virg = str.split(texto3,";")
    texto4 = " ".join(pts_virg)
    '''
    O Primeiro retira os pontos e virgula e o segundo converte a lista formada em string novamente
    '''
    if str.count(texto4,"...") == 0 or str.count(texto4,"...") != 0:
        '''
        Se não há reticências, não há a necessidade de criar um linha pra as reticências.
        '''
        pts = str.split(texto4,".")
        texto5 = " ".join(pts)
        '''
        O Primeiro retira os pontos e o segundo converte a lista formada em string novamente
        '''
        exc = str.split(texto5,"!")
        texto6 = " ".join(exc)
        '''
        O Primeiro retira as exclamações e o segundo converte a lista formada em string novamente
        '''
        ite = str.split(texto6,"?")
        texto7 = " ".join(ite)
        '''
        O Primeiro retira as interrogações e o segundo converte a lista formada em string novamente
        '''
        Resultado = texto7
        ''' 
        Resultado é o texto sem as pontuações em geral.
        '''
        return Resultado
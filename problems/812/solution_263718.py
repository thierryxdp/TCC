def retira_pontuacao(txt):
    '''
    	A função retira a pontuação de uma string informada.
        txt -> str
        str -> str
    '''
    
    txt = txt.replace('-',' ')
    txt = txt.replace(',',' ')
    txt = txt.replace(':',' ')
    txt = txt.replace(';',' ')
    txt = txt.replace('!',' ')
    txt = txt.replace('.',' ')
    txt = txt.replace('?',' ')
    txt = txt.replace('...',' ')
    
    '''
    	Pontuações tiradas:('-', ',', ':', ';', '!', '.', '?' e '...')
    '''
    
    return txt
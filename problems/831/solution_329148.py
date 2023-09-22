def lingua_p (palavra):
    '''
    	essa função recebe uma palavra que e a traduz para a linguagem P
        str-->str
    '''
    x = str.replace(palavra, 'a', 'apa')
    y = str.lower(x)
    return y
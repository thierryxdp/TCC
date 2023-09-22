def hashtag(s):
    '''
    	Funcao que recebe uma string e insere o caractere "#"
        no inicio, no meio e no final
        str -> str
    '''
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
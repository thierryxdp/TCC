def hashtag(s):
    '''Funcao que recebe uma string e inseri o caracter 
    # no inicio, meio e fim da string.
    Dados de entrada: str
    Valor de saida: str
    '''
    meio = (len(s)//2)
    str_Alterada3 = str('#')+s[:meio]+str('#')+s[meio:]+str('#')  
    return str_Alterada3
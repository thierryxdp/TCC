def lingua_p (palavra):
    '''
   
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiouáéíóú':
            vogais = vogais + 'p' + vogais
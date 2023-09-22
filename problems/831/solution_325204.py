def lingua_p(palavra):
    '''lingua_p recebe uma string e devolve outra string
    acrescenta um 'p' depois de cada vogal e acrescenta
    a mesma vogal anterior logo em seguida do 'p'
    str --> str'''
    
    resposta=''
    
    for vogal in palavra:
        if vogal in 'aeiouáéíú':
            vogal = vogal + 'p' + vogal
        resposta = resposta + vogal
    return str.lower(resposta)
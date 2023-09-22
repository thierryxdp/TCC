def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna essa mesma palavra traduzida para a língua do P.
       parâmetro de entrada:str
       valor de retorno:str'''
    nova=''
    for vogal in palavra:
        if vogal in 'AEIOUaeiouãõáéíóúâêîôû':
            vogal=vogal+'p'+vogal
            nova=nova+vogal
        else:
            nova=nova+vogal
    return str.lower(nova)
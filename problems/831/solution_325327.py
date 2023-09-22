def lingua_p(palavra):
    ''' '''
    nova=''
    for vogal in palavra:
        if vogal in 'AEIOUaeiouãõáéíóúâêîôû':
            vogal=vogal+'p'+vogal
            nova=nova+vogal
        else:
            nova=nova+vogal
    return str.lower(nova)
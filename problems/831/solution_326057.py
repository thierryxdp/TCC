def lingua_p(palavra):
    '''função que recebe uma palavra e traduz ela para a lingua do p'''
    '''str-->str'''
    num=''
    for vogal in palavra:
        if vogal in 'aeiouAEIOUáéíõú':
            num=num+vogal+'p'+vogal
        else:
            num=num+vogal
    return num
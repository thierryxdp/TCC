def lingua_p(palavra):
    '''...'''
    pos=1
    for vogal in palavra:
        if vogal in 'aeiouAEIOU':
            pos=palavra.index(vogal)
            palavra=str(palavra[0:pos+1])+'p'+vogal+str(palavra[pos+1:])
    return palavra
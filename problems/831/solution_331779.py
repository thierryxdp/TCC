def lingua_p(palavra):
    '''
    '''
    
    final=''
    
    for letra in palavra:
        final = 'p' + palavra[:len(letra)//2] + 'p' + palavra[len(letra)//2:]+'p'
        
    return final
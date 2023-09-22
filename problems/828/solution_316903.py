def primo(num):
    '''
    Essa função tem como objetivo verificar o numero para se ele for primo
    voltar a resposta um dado booleano'''
    #int -> int -> bool
    
    for i in range((2),(num)):
        if num %i == 0:
        	return False
        i+=1
    return True
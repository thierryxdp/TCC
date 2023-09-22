def primo(numero):
    
    '''Função que retorna se um numero é primo ou não'''
    dibisores = []
    QtDibisores = 0
    dibisoresPossibeis= list(range(1,numero+1))
    ehPrimo = False
    '''reaproveitei boa parte da função anterior aqui'''
    for dibisor in dibisoresPossibeis:
        if numero%dibisor == 0:
            dibisores.append(dibisor)
            
    if len(dibisores) <= 2:
        ehPrimo = True
        return ehPrimo
    else:
        ehPrimo = False
        return ehPrimo
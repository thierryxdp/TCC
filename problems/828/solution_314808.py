def primo(numero):
    dibisores = []
    QtDibisores = 0
    dibisoresPossibeis= list(range(1,numero+1))
    ehPrimo = False
    
    for dibisor in dibisoresPossibeis:
        if numero%dibisor == 0:
            dibisores.append(dibisor)
    	if len(dibisores) < 0:
            ehPrimo = True
    return ehPrimo
def primo(numero):
    dibisores = []
    QtDibisores = 0
    dibisoresPossibeis= list(range(1,numero+1))
    ehPrimo = False
    
    for dibisor in dibisoresPossibeis:
        if numero%dibisor == 0:
            dibisores.append(dibisor)
    	if len(Qtdibisores) <= 2:
            ehPrimo = True
    return ehPrimo
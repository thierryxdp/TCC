def primo(intero):
    dibisores = []
    QtDibisores = 0
    dibisoresPossibeis= list(range(1,numero+1))
    ehPrimo = false
    
    for dibisor in dibisoresPossibeis:
        if numero%dibisor == 0:
            dibisores.append(dibisor)
    	if len(Qtdibisores) <= 2:
            ehPrimo = true
    return ehPrimo
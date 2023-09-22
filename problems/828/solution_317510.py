def primo(Zposit):
    '''função que dado um int positivo(Zposit),retorna um bool 
    dizendo se esse numero é primo(True) ou não(False);
    int->bool'''
    for i in range(2,Zposit-1):
        if Zposit%i==2:
            return True
        else:
            return False
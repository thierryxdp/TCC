def primo(nip):
    '''função que dado um numero inteiro positivo, diz se ele é primo ou não. int ->bool'''
    for x in range(2,nip):
        if nip % x == 0:
            return false
    else:
         return true
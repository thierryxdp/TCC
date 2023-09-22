def uppCons(frase):
    '''função que recebe uma frase e retorna a ela com as consoantes maiúsculas; str=>str'''
    s ="
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyçz':
            s+=caractere.upper()
        else:
            s+=caractere
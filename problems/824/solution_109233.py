def isVogal(c):
    '''Função que recebe uma frase (string) e retorna a mesma frase com todas
    as consoantes maiúsculas e as demais letras como estavam'''
    if c in 'aeiouAEIOUãéáíõóúÃÉÍÕÓÁÚ':
        return True
    else:
        return False
        
def uppCons(frase):
    fraseReturn = ''
    
    cont = 0
    
    while(cont < len(frase)):
        if isVogal(frase[cont]) == False:
            fraseReturn += frase[cont].upper()
        else:
            fraseReturn += frase[cont]
        cont = cont + 1
        
    return fraseReturn
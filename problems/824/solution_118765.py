def uppCons(frase):
    '''função que recebe uma frase e retorna a frase com
    todas as suas consoantes em maiúsculas
    str>>str'''
    proximo=0
    frase_nova=''
    while proximo<len(frase):
        if frase[proximo] in 'qwrtypsdfghjklçzxcvbnm':
            frase_nova=frase_nova+str.upper(frase[proximo])
        else:
            frase_nova=frase_nova+frase[proximo]    
        proximo=proximo+1
    return frase_nova
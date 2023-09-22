def uppCons(frase):
    '''recebe como entrada uma frase e retorn a frase com todas as suas consoantes em maiúscula'''
    proximo=0
    frasenova=''
    
    while proximo<len(frase):
        if frase[proximo] not in 'aeiou':
            str.upper(frase[proximo])
        proximo=proximo+1
    return frase
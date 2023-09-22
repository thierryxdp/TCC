def uppCons(frase):
    '''recebe como entrada uma frase e retorn a frase com todas as suas consoantes em maiúscula'''
    proximo=0
    frasenova=''
    
    while proximo<len(frase):
        if frase[proximo] not in 'aeiouáéíóúâêîôû':
            a=str.upper(frase[proximo])
            frasenova=frasenova+a
        else:
            frasenova=frasenova+frase[proximo]
        proximo=proximo+1
    return frasenova
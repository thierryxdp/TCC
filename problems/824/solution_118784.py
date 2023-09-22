def uppCons(frase):
    '''
    função que recebe uma frase e retorna esta frase com
    todas suas consoantes em maiúsculas
    str--->str
    '''
    numseguinte=0
    resposta=''
    while numseguinte<len(frase):
        if frase[numseguinte] in 'qwrtypsdfghjklçzxcvbnm':
            resposta=resposta+str.upper(frase[numseguinte])
        else:
            resposta=resposta+frase[numseguinte]    
        numseguinte=numseguinte+1
    return resposta
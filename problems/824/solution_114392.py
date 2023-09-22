def uppCons(frase):
    '''
    recebe como entrada uma frase e retorna a frase com
    todas as suas consoantes maiúsculas
   str->str
    '''
    i=0
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            maiuscula=str.upper(frase[i])
            frase=str.replace(frase,frase[i],maiuscula)
        i=i+1
    return frase
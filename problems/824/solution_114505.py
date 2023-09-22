def uppCons(frase):
    ''' funcao recebe uma frase e retorna uma outra frase com
    todas as suas consoantes maiusculas,srt-->str'''
    i=0
    s=''
    while 1<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            s= str.upper(frase[i])
    i=i+1
    return s
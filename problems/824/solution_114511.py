def uppCons(frase):
    ''' funcao recebe uma frase e retorna uma outra frase com
    todas as suas consoantes maiusculas,srt-->str'''
    i=0
    s=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            s += frase[i].upper()
        else:    
    i=i+1
    return s
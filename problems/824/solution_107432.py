def uppCons(frase):
    '''essa função recebe uma frase e retorna somente as consoantes em maiusculas'''
    '''string -> string'''
    frase = list(frase)
    nova_frase = list()
    i = int()
    while(i<len(frase)):
        if(frase[i] in 'BCDFGJKLMNPQRSTVWXZbchdfgjklmnpqrstzxZX'):
            if frase[i] == ' ':
                i +=1
            frase[i] = frase[i].upper()
        i += 1
    return ''.join(frase)
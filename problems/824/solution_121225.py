def uppCons(frase):
    '''Recebe uma frase e retorna a frase com todas as consoantes
    em maiusculas'''
    '''str->str'''
    frasenova=''
    for i in frase:
        if i in 'bcdfghjklmmpqrstvxwyzç':
            frasenova+=i.upper()
        else:
            frasenova+=i
    return frasenova
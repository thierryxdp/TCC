def lingua_p(palavra):
    '''
    recebe uma palavra em portugues e retorna essa palavra
    traduzida para a lingua do p
    str->str
    '''
    p=''
    for i in palavra:
        if i in 'AEIOUÁÉÍÓÚÂÊÔÃÕaeiouáéíóúâêôãõ':
            p=p+i+'p'+ i
        if i not in 'AEIOUaeiou':
            p=p+i
    return str.lower(p)
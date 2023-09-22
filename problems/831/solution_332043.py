def lingua_p(palavra):
    '''
    funcao que recebe uma palavra em portugues e retorna essa
    palavra traduzina na lingua do P, em que depois de cada
    vogal é inserida a letra p + a vogal anterior
    string->string
    '''
    x=str.lower(palavra)
    string=''
    consoantes='bcdfghjklmnpqrstvwxyz'
    for y in x:
        string=string+y
        if y not in consoantes:
            string=string+'p'+y
    return string
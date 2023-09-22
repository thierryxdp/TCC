def Maiuscula(l):
    """ Recebe uma letra e retorna se ela é ou não uma consoante"""
    if l in  ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
        return 'true'
    else:
        return 'false'
def uppCons(frase):
    """ Recebe uma frase e retorna a mesma com suas letras consoantes em caixa
alta e suas vogais igual a frase original"""
    for e in frase:
        if Maiuscula(e) == 'true':
            str.replace(frase,e,str.upper(e))
            return frase
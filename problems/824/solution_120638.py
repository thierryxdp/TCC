def Maiuscula(l):
    """ Recebe uma letra e retorna se ela é ou não uma consoante"""
    if l in  ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
        return 'true'
    else:
        return 'false'
def listaconsoante(frase):
    """ Recebe uma frase e retorna suas consoantes"""
    list(frase)
    R = []
    for e in frase:
        if Maiuscula(e) == 'true':
            list.append(R,e)
    return R
def listavogal(frase):
    """ Recebe uma frase e retorna suas consoantes"""
    list(frase)
    R = []
    for e in frase:
        if Maiuscula(e) == 'false':
            list.append(R,e)
    return R
def uppCons(frase):
    """ Recebe uma frase e retorna a mesma com as consoantes 
    em caixa alta"""
    list(frase)
    R = list.extend(listaconsoante(frase),listavogal(frase))
    return str(R)
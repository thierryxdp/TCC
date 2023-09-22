#QUESTAO2
def uppCons(frase):
    '''
    A função retorna todas as consoantes
    em maiusculo.
    list -> string
    '''
    i=0
    frase = frase[0]
    consoantes = ['b','c','d','f','g','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    while i<len(frase):
        if frase in consoantes:
            frase = frase.repalce(consoante.upper)
        i = i +1
    return frase
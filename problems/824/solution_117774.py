def substituir(letra):
    '''Funcao para transformar uma consoante minúscula em maiúscula;
    str->str'''
    consoantes=['b','c','d','f','g','h','j'
                 'k','l','m','n','p','q','r',
                 's','t','v','w','x','y','z','ç']
    if letra in consoantes:
        return str.upper(letra)
    else:
        return letra
    
    
def uppCons(frase):
    '''Retorna a frase com as consoantes em caixa alta;
    str->str'''
    
    frase="".join(map(substituir,frase))
    return frase
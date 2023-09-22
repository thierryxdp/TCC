def retira_pontuacao(frase):
    '''Retorna a frase sem nenhuma pontuação;
    str->str'''
    if frase[:]=='.':
        list.del(frase,[:])
    elif frase[:]==',':
        list.del(frase,[:])
    elif frase[:]==':':
        list.del(frase,[:])
    elif frase[:]=='-':
        list.del(frase,[:])
    elif frase[:]=='!':
        list.del(frase,[:])
    elif frase[:]=='?':
        list.del(frase,[:])
    elif frase[:]==3*'.':
        list.del(frase,[:])
        
    return frase
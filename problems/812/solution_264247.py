def retira_pontuacao(frase):
    '''Retorna a frase sem nenhuma pontuação;
    str->str'''
    
    if frase[:]=='.':
        return list.del(frase,[:])
    elif frase[:]==',':
        return list.del(frase,[:])
    elif frase[:]==':':
        return list.del(frase,[:])
    elif frase[:]=='-':
        return list.del(frase,[:])
    elif frase[:]=='!':
        return list.del(frase,[:])
    elif frase[:]=='?':
        return list.del(frase,[:])
    elif frase[:]==3*'.':
        return list.append(frase,' ')
        
    return frase
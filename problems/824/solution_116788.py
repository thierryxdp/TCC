def uppCons(frase):
    '''Função que retorna a frase de entrada com todas e 
apenas as suas consoantes em maiúsculas;
    str -> str'''
    f=''
    indice=0
    while indice<len(frase):
        if frase[indice] in ['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            f+=str.upper(frase[indice])
        else:
            f+=frase[indice]
        indice=indice+1
    return f
def uppCons(frase):
    """Função  que recebe uma frase e retorna todas as consoantes em maiúcula
    str -> str"""
    i=0
    string=''
    while i<len(frase):
        if frase[i] in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v''x','w','y','z']:
            string=string + frase[i].upper()
        else:
            string=string + frase[i]
        i=i+1
    return string
def uppCons(frase):
    """função que recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas
    string -> string"""
    letra=0
    consoante=''
    while letra<len(frase):
        if frase[letra] in 'bcdfghjklmnpqrstvxwyzç':
           consoante+=str.upper(frase[letra])
        else:
             consoante+=frase[letra]
        letra+=1
    return consoante
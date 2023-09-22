def uppCons(frase):
    """ Recebe uma frase e retorna a frase com as consoantes em maiúsculas. Str-->Str"""
    vogais = ['a','e','i','o','u','y','á','â' ,'ã' ,'à' , 'é' ,'è' ,'ê' , 'í' ,'ì', 'î' , 'ò' ,'ó' ,'ô' ,'õ' ,'ú' ,'ù' ,'û' ]
    resposta = []
    for i in range(len(frase)):
        if frase[i] in vogais:
            resposta.append(frase[i])
        else:
            resposta.append(frase[i].upper())
    return "".join(resposta)
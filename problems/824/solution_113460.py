def uppCons(frase):
    """função que recebe uma frase e retorna elas com todas as 
    consoantes em maiúsculo:str->str"""
    i=0
    resposta=''
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            resposta + str.upper(frase[i])
        i=i+1
        return resposta
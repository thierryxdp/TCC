def uppCons (frase):
    '''função que recebe como entrada uma frase e rotorna essa
    frase com todas as consoantes MAIÚSCULAS, e o resto da fra
    se original, str->str'''
    consoante=0
    resposta=''
    while consoante<len(frase):
        if frase[consoante] in'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvyxz' :
            resposta+=str.upper(frase[consoante])
            resposta=str.replace(resposta,frase,frase)
    	consoante+=1
    return resposta
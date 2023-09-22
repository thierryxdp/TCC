# Dada uma frase, esta função retorna uma frase semelhante a primeira, porém
# com todas as consoantes maiúsuculas.
# str -> str

def uppCons(frase):
    i = 0
    resposta = ''
    
    while i<len(frase):
        if frase[i] in 'AEIOUaeiouàÀáÁâÂãÃéÉêÊíÍÓóôÔúÚ':
            resposta = resposta + frase[i]
        else:
            resposta = resposta + str.upper(frase[i])
        i = i+1
        
    return resposta
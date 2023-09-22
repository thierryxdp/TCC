def maiusculaCons(frase):
    frase = frase if frase not in 'AEIOUaeiouàÀáÁâÂãÃéÉêÊíÍÓóôÔúÚ' else str.upper(str(frase))

def uppCons(frase):
    frase = list(frase)
    frase = list(map(maiusculaCons, frase))
    resposta = ''
    for i in range(len(frase)):
        resposta += str(frase[i])
    
    return resposta
#Entrada: Uma frase 
#Precisamos analisar cada letra da frase
#Ao encontrar as consoantes, passamos para maiúsculo
def uppCons(frase:str)->str:
    """Recebe uma frase e transforma todas as 
    conoantes em maiúsculo"""
    fraseAlterada=list()
    tamanho=len(frase)
    i=0
    while i < tamanho:
        if (str.lower(frase) in "aeiou" == True):
            list.append(frasealterada, frase[i])
        else:
            list.append(frasealterada, str.upper(frase[i]))
        i+=1
    return str.join(frasealterada)
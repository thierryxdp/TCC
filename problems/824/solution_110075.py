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
        if (str.lower(frase[i]) in "aeiou" == False):
            list.append(fraseAlterada, str.upper(frase[i]))
        else:
            list.append(fraseAlterada, frase[i])
        i+=1
    return str.join("",fraseAlterada)
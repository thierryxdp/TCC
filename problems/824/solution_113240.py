def uppCons(frase):
    '''recebe uma frase e retorna a mesma frase com todas as 
    consoantes em maiusculo e os demais caracteres exatamente 
    como na frase original
    entrada: str
    saida: str'''
    i=0
    vogal=''
    while i<len(frase):
        if frase[i] in "AEIOUaeiouãõóáúíé":
            vogal = vogal + frase[i]
        if frase[i] in "BCDFGHJKLMNPQRSTVXZÇbcdfghjklmnpqrstvxzç,.!?- ":
            a=frase[i].upper()
            vogal = vogal + a
        i=i+1
    return vogal
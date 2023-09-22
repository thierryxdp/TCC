def posLetra(Str,Let,Num):
    """
    recebe uma string, uma letra e a ocorrência desejada. retorna o índice
    no qual a enésima ocorrência dessa letra no string se encontra.
    """
    i=0
    lista=[]
    
    while i<len(Str):
        if Str[i]==Let:
            list.append(lista,Let)
        if len(lista)==Num:
            return i
        i=i+1
    if len(lista)<Num:
        return -1
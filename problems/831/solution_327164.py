def lingua_p(palavra: str):
    pos=0
    strPe=''
    for caractere in palavra:
        if caractere in 'AEIOUaeiou':
            pos=pos+1
            strPe=strPe.Insert(pos,p)
    return pe
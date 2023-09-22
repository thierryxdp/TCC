def lingua_p(palavra: str):
    pos=0
    pe=''
    for caractere in palavra:
        if caractere in 'AEIOUaeiou':
            pos=pos+1
            palavra=palavra.Insert(pos,p)
    return pe
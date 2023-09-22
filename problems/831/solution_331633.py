def lingua_p(palavra):
    i=0
    for d in palavra:
        if d in 'AEIOUaeiou':
            palavra=list(palavra)
            list.insert(palavra,i+1,'p'+d)
            i=i+2
        else:
            i=i+1
    palavra=(' '.join(palavra))
    palavra=str.replace(palavra,' ','')
    return palavra
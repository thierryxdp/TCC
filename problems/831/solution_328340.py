def lingua_p(palavra):
    i=0
    
    for i in range(len(palavra)):
        if palavra[i]in'AEIOUaeiou':
            palavra=list(palavra)
            palavra=palavra.append('p',i+1)
            palavra=palavra.append(palavra[i],i+2)
    return palavra
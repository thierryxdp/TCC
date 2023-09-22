def uppCons(frase):
    
    t=0
    consoantes=''
    while t< len(frase):
        if frase[t] not in 'AEIOUaeiou':
            consoantes= consoantes+str.upper(frase[t])
            t = t +1
        if frase[t] in 'AEIOUaeiou':
            consoantes= consoantes + frase[t]
            t = t + 1
        
    return consoantes
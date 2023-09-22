def uppCons(frase):
 
    i=0
    consoantes=''
    while i<len(frase):
        if texto[i] in 'qwrtypsdfghjklçzxcvbnm':
            consoantes=consoantes+frase[i]
        i=i+1
    return frase
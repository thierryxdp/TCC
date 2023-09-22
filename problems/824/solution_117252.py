def uppCons(frase):
 
    i=0
    consoantes=''
    s=str.split(frase)
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            
            
            consoantes=consoantes+frase[i]
        i=i+1
    return  s
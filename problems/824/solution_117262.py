def uppCons(frase):
 
    i=0
    consoantes=''
    s=str.split(frase)
    p=str.partition(frase,qwrtypsdfghjklçzxcvbnm)

    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            
            
            consoantes=consoantes+frase[i]
        i=i+1
    return  p
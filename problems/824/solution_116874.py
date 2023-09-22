def uppCons(frase):
    i=0
    consoantes=''
    resto=''
    while i < len(frase):
        if str.upper(frase[i]) not in 'aeiouAEIOU':
            consoantes+= frase[i]
        else:
            resto+=frase[i]
        i+=1
          
    return consoantes, resto
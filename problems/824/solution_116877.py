def uppCons(frase):
    i=0
    consoantes=''
    while i < len(frase):
        if str.upper(frase[i]) in 'QWRTYPLKJHGFDSZXCVBNÇM':
            consoantes+= str.upper(frase[i])
        else:
            consoantes+=frase[i]
        i+=1
          
    return consoantes
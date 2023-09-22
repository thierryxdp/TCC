def uppCons(frase):
    x=0
    consoantes=''
    while x<len(frase):
        if frase[x] not in 'AEIOUaeiouáéíóúÁÉÍÓÚ':
            consoantes= consoantes +str.upper(frase[x])
            x = x +1
            elif x< len(frase):
                frase[x] in 'AEIOUaeiouáéíóúÁÉÍÓÚ'
                consoantes= consoantes  + frase[x]
                x = x +1
                return consoantes
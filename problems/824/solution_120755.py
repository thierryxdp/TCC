def uppCons(frase):
    texto=''
    i=0
    letra=frase[i]
    while i<len(frase):
        if letra in 'bcdfghjklmnpqrstvxwyz':
            texto = texto + (str.upper(frase,letra))
            i=i+1
            
            return texto
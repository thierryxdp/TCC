def uppCons(frase):
    h=''
    i=0
    while i<len(frase):
        if frase[i] in 	'qwrtyhpçlkjhgfdszxcvbnm':
            h= h+frase[i].upper()
            else:
            h=h+frase[i]
        i=i+1
    return h
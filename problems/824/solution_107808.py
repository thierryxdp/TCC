def uppCons(string):
    vogais=""
    i=0
    proximo=0
    while proximo<len(string):
        if string[i] in 'bcdfgjklmnpqrstvwxz':
            i=i+1
            proximo=proximo+1
            vogais=vogais+str.upper(string[i])
        else:
            return vogais
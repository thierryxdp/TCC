def uppCons(string):
    vogais=""
    i=0
    proximo=0
    while proximo<len(string):
        if string[i] in 'bcdfgjklmnpqrstvwxz':
            vogais=vogais+str.upper(string[i])
        i=i+1
        proximo=proximo+1
        else:
            vogais=vogais+(string[i])
    return vogais
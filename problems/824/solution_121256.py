def uppCons(frase):
    for i in range(len(frase)):
        if frase[i]!='a'and'b'and'c'and'd'and'e'and'A'and'B'and'C'and'D'and'E':
            str.replace(frase,frase[i],str.upper(frase[i]))
        return frase
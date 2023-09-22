def uppCons(frase):
    string1= ''
    c = ''
    for i in frase:
        if(i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u'):
            i = i.upper()
            string1 += i
        else:
            string1 += i
    return string1
def uppCons(frase):
    string1= ''
    c = ''
    for i in frase:
        if(i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and
           i != 'á' and i != 'é' and i != 'í' and i != 'ó' and i != 'ú' and
           i != 'ã' and i != 'ê' and i != 'î' and i != 'ô' and i != 'û' and
           i != 'â' and i != 'õ'):
            i = i.upper()
            string1 += i
        else:
            string1 += i
    return string1
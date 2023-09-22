def uppCons(frase):
    frasen=[]
    cont=0
    while cont<len(frase):
        if frase[cont]=='a' or frase[cont]=='A' or frase[cont]=='e' or frase[cont]=='E' or frase[cont]=='i' or frase[cont]=='I' or frase[cont]=='o' or frase[cont]=='O' or frase[cont]=='u' frase[cont]=='U':
            list.append(frasen,frase[cont])
        else:
            list.append(frasen,str.upper(frase[cont]))
        cont+=1
    return str.join("",frasen)
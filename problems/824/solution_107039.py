def uppCons(frase):
    frasen=[]
    cont=0
    vogais=["a","A","e","E","i","I","o","O","u","U"]
    import unidecode 
    semacen=unidecode.unidecode(frase)
    while cont<len(frase):
        if semacen[cont] in vogais:
            list.append(frasen,frase[cont])
        else:
            list.append(frasen,str.upper(frase[cont]))
        cont+=1
    return str.join("",frasen)
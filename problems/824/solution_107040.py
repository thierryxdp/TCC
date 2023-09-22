def uppCons(frase):
    frasen=[]
    cont=0
    '''vogais=["a","A","á","Á","à","À","ã","Ã","â","Â","e","E","é","É","è","È","ê","Ê","i","I","í","Í","ì","Ì","î","Î","o","O","ó","Ó",
    while cont<len(frase):
        if :
            list.append(frasen,frase[cont])
        else:
            list.append(frasen,str.upper(frase[cont]))
        cont+=1
    return str.join("",frasen)
    '''
    from unidecode import unidecode
    return unidecode(frase)
def uppCons(frase):
    frasen=[]
    cont=0
    vogais=["a","A","á","Á","à","À","ã","Ã","â","Â","e","E","é","É","è","È","ê","Ê","i","I","í","Í","ì","Ì","î","Î","o","O","ó","Ó","ò","Ò","õ","Õ","ô","Ô","u","U","ú","Ú","ù","Ù","û","Û"],
    while cont<len(frase):
        if frase[cont] in vogais:
            list.append(frasen,frase[cont])
        else:
            list.append(frasen,str.upper(frase[cont]))
        cont+=1
    return str.join("",frasen)
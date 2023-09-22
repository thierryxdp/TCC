def uppCons(frase):
    frasen=[]
    cont=0
    while cont<len(frase):
        if frase[cont]=="a" or frase[cont]=="A" or frase[cont]=="á" or frase[cont]=="Á" or frase[cont]=="à" or frase[cont]=="À" or frase[cont]=="ã" or frase[cont]=="Ã" or frase[cont]=="â" or frase[cont]=="Â" or frase[cont]=="e" or frase[cont]=="E" or frase[cont]=="é" or frase[cont]=="É" or frase[cont]=="è" or frase[cont]=="È" or frase[cont]=="ê" or frase[cont]=="Ê" or frase[cont]=="i" or frase[cont]=="I" or frase[cont]=="í" or frase[cont]=="Í" or frase[cont]=="ì" or frase[cont]=="Ì" or frase[cont]=="î" or frase[cont]=="Î" or frase[cont]=="o" or frase[cont]=="O" or frase[cont]=="ó" or frase[cont]=="Ó" or frase[cont]=="ò" or frase[cont]=="Ò" or frase[cont]=="õ" or frase[cont]=="Õ" or frase[cont]=="ô" or frase[cont]=="Ô" or frase[cont]=="u" or frase[cont]=="U" or frase[cont]=="ú" or frase[cont]=="Ú" or frase[cont]=="ù" or frase[cont]=="Ù" or frase[cont]=="û" or frase[cont]=="Û":
            list.append(frasen,frase[cont])
        else:
            list.append(frasen,str.upper(frase[cont]))
        cont+=1
    return str.join("",frasen)
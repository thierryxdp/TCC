def inverte(frase):
    excl = frase.replace("!"," ")
    inte = excl.replace("?"," ")
    virg = inte.replace(","," ")
    trav = virg.replace("-"," ")
    pont = trav.replace("."," ")
    split = str.split(pont)
    cont = split[-1:-(len(split)+1):-1]
    x = cont.join(" ")
    return str.lower(x)
def uppCons(frase):
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    toUpper = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R",
               "S","T","V","W","X","Y","Z","b","c","d","f","g","h",
               "j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    array = list(frase)
    for i,c in enumerate(array):
        if c in toUpper:
            array[i] = c.upper()
    return ("".join(array))
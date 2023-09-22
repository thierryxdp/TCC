def linguap(palavra):
    palavra2 = ""
    for letra in palavra:
        if letra in "AEIOUaeiouàèìòùáéíóúãõâêîôûÂÊÎÔÛÁÉÍÓÚÀÈÌÒÙÃÕ":
            palavra2 += letra+'p'+letra
        else:
            palavra2 += letra
    return palavra2
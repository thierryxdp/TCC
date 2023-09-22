def conta_frases(texto):
    if "!" in texto:
        lista=[str.split(texto,"!")]
        if "." in lista:
            lista=[str.split(lista,".")]
            if "?" in lista:
                lista=[str.split(lista,"?")]
                if "..." in lista:
                    lista=[str.split(lista,"...")]
                    return len(lista)
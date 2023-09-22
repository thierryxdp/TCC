def conta_frases(texto):
    if "!" in texto:
        lista=[str.split(texto,"!")]
        elif "." in lista:
            lista=[str.split(lista,".")]
            elif "?" in lista:
                lista=[str.split(lista,"?")]
                elif "..." in lista:
                    lista=[str.split(lista,"...")]
                    return len(lista)
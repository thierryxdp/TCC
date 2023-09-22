def uppCons(frase):
    """..."""
    i = 0
    fraseCons = []

    while(i < len(frase)):
        if ("bcdfghjklmnpqrstvwxyzç" in frase[i]):
            fraseCons[len(fraseCons):len(fraseCons)] = [str.upper(frase[i])]

        else:
            fraseCons[len(fraseCons):len(fraseCons)] = [frase[i]]
        i += 1

    fraseCons = str.join('',fraseCons)

    return fraseCons
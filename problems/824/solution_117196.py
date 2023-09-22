def uppCons(texto):
    texto=str.upper(texto)
    texto=str.replace(texto,'A','a')
    texto=str.replace(texto,'E','e')
    texto=str.replace(texto,'I','i')
    texto=str.replace(texto,'O','o')
    texto=str.replace(texto,'U','u')
    return texto
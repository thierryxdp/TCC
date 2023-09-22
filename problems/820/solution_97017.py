def posLetra(string,letra,numero):
    """retorna em que posição da string a ocorrência da letra está
    caso não alcance a ocorrência pedida retorna -1;
    string, string, int -> int"""
    string = sorted(string)
    return string.count(letra)
def conta_frases(texto):
    return int(len(str.split(texto,'.')) + int(len(str.split(texto,',')) + int(len(str.split(texto,'...')) + int(len(str.split(texto,'!'))
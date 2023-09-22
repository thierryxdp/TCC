def conta_frases(texto):
    'dado um texto retorne a quantidade de frases que existam no texto.str-->int'
    texto=str.replace(str.replace(str.replace(str.replace(texto,'!','#'),'.','#'),'?','#'),'...','#')
    return len(str.split(texto,'#'))
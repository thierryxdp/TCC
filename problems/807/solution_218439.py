def conta_frases(texto):
    (texto1) = str.split(texto,".")
    (texto2) = str.split(texto1,"!")
    (texto3) = str.split(texto2,".")
    (texto4) = str.split(texto3,".")
    return len(texto)
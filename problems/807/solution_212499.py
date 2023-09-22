def conta_frases(texto):
    pnto = texto.split(".")
    excl = texto.split("!")
    inte = texto.split("?")
    reti = texto.split("...")
    return len(pnto)+len(excl)+len(inte)+len(reti)
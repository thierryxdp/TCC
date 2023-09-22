def lingua_p(palavra):
    texto=""
    for letra in palavra:
        if letra in "AÁÃÂEÉÊIÍOÓÕÔUÚaáãâeéêiíoóõôuú":
            texto = texto + letra + "p" + letra
        if letra not in "AÁÃÂEÉÊIÍOÓÕÔUÚaáãâeéêiíoóõôuú":
            texto = texto + letra
    return texto
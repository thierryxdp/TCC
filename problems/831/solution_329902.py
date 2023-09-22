def lingua_p(palavra):
    """função que recebe como parametro uma palavra e retorna a mesma palavra traduzida para lingua do p; str->str"""
    P=''
    for letra in palavra:
        P += letra
        if letra in "aàâãáeêèéiìîíoóòõôùúu":
            P += "p"+ letra
    return P
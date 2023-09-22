def lingua_p(palavra):
    nova=""
    for letra in palavra:
        if letra in "AEIOUaáeéiíoóuúàâêô":
            nova=nova+letra+"p"+letra
        else:
            nova=nova+letra
    return str.lower(palavra)
def uppCons(frase):
    nova_frase = ""
    for letra in frase:
        if letra in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â'] or letra in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ã', 'Õ', 'Â']:
            nova_frase += letra.lower()
        else:
            nova_frase += letra.upper()
    return nova_frase[0].upper() + nova_frase[1:]
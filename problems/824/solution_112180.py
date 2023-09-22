def vogal(letra):
    vogal=['a','e','i', 'o','u']
    if letra not in vogal:
        nv_letra=letra.upper()
    return nv_letra
def uppCons(frase):
    for i in range(len(frase)):
        if frase[i] not in vogal:
            letra=str(map(str.upper(),frase[i]))
        nv_frase+=letra
    return nv_frase
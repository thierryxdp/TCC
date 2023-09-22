def uppCons(frase):
    vogal = 0
    separar = str(list(frase))
    while vogal<5:
        if separar!='a':
            separar.upper(separar-'a')
        vogal = vogal + 1
    return frase
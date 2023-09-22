def lingua_p(palabra): 
    degon = palabra.split(
    vogal = 'aeiouáéíóú'
    for vogal in palabra:
        epile = palabra[0:len(palabra[vogal])]
        sia = palabra[len(palabra[vogal].index):len(palabra)]
        degon = epile + 'p' + sia
    return degon.lower
def lingua_p(palabra): 
    degon = ''
    for vogal in palabra:
        epile = palabra[0:(palabra[vogal])+1]
        sia = palabra[(palabra[vogal])+1:len(palabra)]
        degon = str(epile) + 'p' + str(sia)
    return degon
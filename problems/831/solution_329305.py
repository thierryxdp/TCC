def lingua_p(palabra): 
    degon = ''
    for vogal in palabra:
        epile = palabra[0:vogal+1]
        sia = palabra[vogal+1:len(palabra)]
        degon = epile + 'p' + sia
    return degon
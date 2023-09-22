def inverte(frase):
    '''Recebe frase e retorna frase ao contrário e sem pontuacao. Dizer a frase entre aspas. str-->str'''
    if ":" in frase:
        frase = frase.replace(":","")
    if ";" in frase:
        frase = frase.replace(";","")
    if "." in frase:
        frase = frase.replace(".","")
    if "!" in frase:
        frase = frase.replace("!","")
    if "-" in frase:
        frase = frase.replace("-","")
    if "," in frase:
        frase = frase.replace(",","")
    if "?" in frase:
        frase = frase.replace("?","")
        
    fragelist = frase.split(" ")
    range_list = len(fragelist)+1
    fat_inv = fraselist[1:-(range_list):-1]
    inverso = str.join(' ', fat_inv)
    return str.lower(inverso)
def lingua_p(palabra):
	'''função que retorna palavra traduzida na língua do p.
    str--> str'''
    listola = []
    palabraNoba = [] 
	for letra in palabra:
        listola.append(letra)
    for vogogal in listola:  
        if vogogal in 'aeiouáéíóú':  
            palabraNoba.append(vogogal + 'p' + vogogal)  
        else: 
            palabraNoba.append(vogogal)
    
	linguaP = ''.join(palabraNoba)
    return linguaP.lower()
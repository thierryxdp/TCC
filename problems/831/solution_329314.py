def lingua_p(palabra):
	'''função que retorna palavra traduzida na língua do p.
    str--> str'''
    
    palabraNoba = []  

    for vogogal in list(palavra):  
        if vogogal in 'aeiouáéíóú':  
            palabraNoba.append(vogogal + 'p' + vogogal)  
        else: 
            palabraNoba.append(vogogal)
            
	linguaP = palabraNoba.join()
    return linguaP.lower
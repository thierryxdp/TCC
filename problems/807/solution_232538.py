def conta_frases(texto):
    '''Dado um texto retorna o número de frases presentes nele
    string -> int'''
	
    txt1 = texto.replace('...','~')
    txt2 = txt1.replace('?','~')
    txt3 = txt2.replace('!','~')
    txt4 = txt3.replace('.','~')
    
    return len(txt4.split('~'))-1
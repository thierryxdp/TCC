conta_frases(texto):
    '''Dado um texto retorna o número de frases presentes nele
    string -> int'''
	
   	rtc = texto.replace('...','§')
    itr = rtc.replace('?','§')
    exc = itr.replace('!','§')
    ptf = exc.replace('.','§')
    
    return len(ptf.split('§'))-1
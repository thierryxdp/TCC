def conta_frases(texto):
    
	cnt1 = texto.split(’.’)
	cnt2 = texto.split(’!’)
	cnt3 = texto.split(’?’)
	cnt4 = texto.count(’...’)
	
    return (len(cnt1) - 2*cnt4) + len(cnt2) + len(cnt3) - 3
def lingua_p (palavra):
    if contains(palavra, 'a'):
        palavra = palavra.replace('a', 'apa')
    if contains(palavra, 'e'):
        palavra = palavra.replace('e', 'epe')
    if contains(palavra, 'i'):
        palavra = palavra.replace('i', 'ipi')    
	if contains(palavra, 'o'):
        palavra = palavra.replace('o', 'opo')    
    if contains(palavra, 'u'):
        palavra = palavra.replace('u', 'upu')    
		return palavra
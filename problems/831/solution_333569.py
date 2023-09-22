from operator import contains
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
	if contains(palavra, 'á'):
        palavra = palavra.replace('á', 'ápá')
    if contains(palavra, 'é'):
        palavra = palavra.replace('é', 'épé')
    if contains(palavra, 'í'):
        palavra = palavra.replace('í', 'ípí')    
	if contains(palavra, 'ó'):
        palavra = palavra.replace('ó', 'ópó')
    if contains(palavra, 'ú'):
        palavra = palavra.replace('ú', 'úpú')
    return palavra
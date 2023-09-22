def inverte(frase):
	''' Essa função retora uma frase invertida e sem pontuações
	informar frase entre aspas
	string -> string '''
	frase = frase.replace(':','')
	frase = frase.replace(';','')
	frase = frase.replace('.','')
	frase = frase.replace('!','')
	frase = frase.replace('-','')
	frase = frase.replace(',','')
	frase = frase.replace('?','')
    
	frase_list = frase.split(' ')
	range_list = len(frase_list) +1
	fat_inv = frase_list[-1:-(range_list):+1]
	inverso = str.join(' ',fat_inv)
	return str.lower(inverso)
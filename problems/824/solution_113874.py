def uppCons(texto):
    
	i=0
    vogais=''
    
    while i<len(texto):
        if texto[i] in 'QWRTYPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm':
            vogais=vogais+texto[i]
        i=i+1
    return vogais
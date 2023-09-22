def conta_frases(frs):
    #return str.count(frs,'.') or str.count(frs,'.') or str.count(frs,'...') or str.count(frs,'...') + str.count(frs,'!') + str.count(frs,'?')
	if '.'and'.'and'...' in frs:
        return str.count(frs,'.') or str.count(frs,'.') or str.count(frs,'...') or str.count(frs,'...') + str.count(frs,'!') + str.count(frs,'?')
    
    elif '.'and'...' in frs:             
        return  str.count(frs,'.') or  str.count(frs,'...') or str.count(frs,'!') or str.count(frs,'?')
    
    elif '.'and'.'and'...' in frs:
        return  str.count(frs,'.') or str.count(frs,'.') or  or str.count(frs,'...') or str.count(frs,'!') or str.count(frs,'?')
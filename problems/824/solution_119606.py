def uppCons(f):
    
    r = []
    for i in range(len(f)):
        if f[i] in 'bcdfghjklmnopqrstuvwxyz':
        	f[i] = str.upper(f[i])
	return f
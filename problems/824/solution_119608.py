def uppCons(f):
    
    r = []
    for i in range(len(f)):
        if f[i] in 'bcdfghjklmnpqrstvwxyz':
        	f = f[0:i] + str.upper(f[i]) + f[i+1:]
	return f
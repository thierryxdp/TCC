def uppCons(f):
    
    r = []
    for i in range(len(f)):
        if f[i] in 'bcçdfghjklmnpqrstvwxyz':
        	f = f[0:i] + str.upper(f[i]) + f[i+1:]
	return f
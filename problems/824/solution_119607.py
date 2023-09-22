def uppCons(f):
    
    r = []
    for i in range(len(f)):
        if f[i] in 'bcdfghjklmnopqrstuvwxyz':
        	f = f[0:i] + str.upper(f[i]) + f[i:]
	return f
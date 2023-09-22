def uppCons(X=str):
    Y=0
    R=''
    while Y<len(X):
        if X[Y] not in 'AEIOUaeiou':
            R=R+str.upper(X[Y])
        if X[Y] in 'AEIOUaeiou':
            R=R+(X[Y])
        Y=Y+1
	return R
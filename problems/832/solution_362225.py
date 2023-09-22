def eh_quadrada(X):
    for i, linha  in enumerate(X):
        if len(linha)!=len(X):
            return False
        for j in range(i):
            if linha[j]!=X[j][i]:
                return False
            else:
            	return True
            return True
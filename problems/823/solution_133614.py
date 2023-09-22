def faltante(pecas):
    N = len(pecas)
    
    for i in range(N):
    	if i not in pecas:
            return i
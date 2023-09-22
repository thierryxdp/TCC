# Dada uma matriz M, esta função retorna a informação se M é quadrada ou não.
# Um matriz vazia é considerada quadrada.
# list(list) -> bool

def eh_quadrada(m):
    if (len(m) == len(m[0])) or (len(m)==0) :
        resp = True
    else:
        resp = False
        
	return resp
'''dado uma tupla com 4 elementos int filtra cada elemento 1 por 1 e
retorna uma nova tupla apenas com elementos pares.
tuple -> tuple'''
def filtra_pares(a):
    newtuple= ()
    
    if a[0]%2==0:
        newtuple= newtuple + (a[0],)
    	if a[1]%2==0:
        	newtuple= newtuple + (a[1],)
   			if a[2]%2==0:
       			newtuple= newtuple + (a[2],)
   				if a[3]%2==0:
    				newtuple= newtuple + (a[3],)
        
        			return newtuple
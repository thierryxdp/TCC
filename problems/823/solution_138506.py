1	def faltante(n):
2	    x=0
3	    z=1
4	    while len(n)-1>=n[x]:
5	        if n[0] == n[1]:
6	            return n[x]
7	        x=x+1
8	        z=z+1
9	    return z
10
def fatorial(n):
    x=list(range(n))
    y=0
    while y<len(x):
      	x[y]=x[y]*x[y+1]
  	  	y=y+1
    return x[y]
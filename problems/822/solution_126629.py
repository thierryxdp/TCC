def repetidos (num):
    i=0
    pares=0
  	while i<len(num):
        if num[i]==num[i+1]:
           i+=1
           pares+=1
        else:
           i+=1
    return pares
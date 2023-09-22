def colchao (medidas, H, L):
    [ A, B, C ] = medidas
    if C > H:
   	 return False
	if C > L:
     return False
	if A > H:
      return False
	if A > L:
      return False
	else:
     return True
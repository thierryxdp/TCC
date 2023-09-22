def colchao (medidas, H, L):
    [ A, B, C ] = medidas
    if C > H:
   	 return False
	if C > L:
     return False
	if B > H:
      return False
	if B > L:
      return False
	else:
     return True
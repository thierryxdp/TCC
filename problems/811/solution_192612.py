def colchao (medidas, H, L):
    [ A, B, C ] = medidas
    if A > H:
   	 return False
	if A > L:
     return False
	if B > H:
      return False
	if B > L:
      return False
	if B >= H:
      return True
    else:
     return True
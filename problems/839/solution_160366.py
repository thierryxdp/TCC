def carros (pessoas, capacidade=5):
   if 0 < pessoas<= capacidade :
   		return (capacidade%pessoas)
   
   elif 0==pessoas:
        return 0
    
   elif pessoas % capacidade != 0:
    	return ((pessoas//capacidade)+1)
def carros (pessoas, capacidade=5):
   if 0 < pessoas<= 5 :
   		return 1
   
   elif 0==pessoas:
        return 0
    
   elif pessoas % capacidade != 0:
    	return ((pessoas//capacidade)+1)
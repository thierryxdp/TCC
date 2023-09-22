def carros (pessoas, capacidade=5):
   if pessoas<= 5:
   		return 1
    
   elif pessoas > 5 and pessoas% 5!= 0:
    	return ((pessoas//5)+1)
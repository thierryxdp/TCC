def repetidos (nums):
    i=0
    pares=0
  	#while i<len(nums):
        if nums[i]==nums[i+1]:
         	i+=1
        	pares+=1
     	else:
    	    i+=1
  	return pares
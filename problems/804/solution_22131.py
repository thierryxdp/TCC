test_list = [(6, 4, 2, 8), (5, 6, 7, 6), (8, 0, 2), (7, )] 
  
    res_list = [] 
for sub in test_list: 
    res = True 
      
    
    for ele in sub: 
        if ele % 2 != 0: 
            res = False
            break
    if res: 
        res_list.append(sub)
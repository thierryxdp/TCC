def repetidos(n):
    index= 1
    repetidos= 0
    
    while index < len(palavra):
        if n[index] == n[index -1]:
              repetidos +=1
                index+=1
                
        else:
            index+=1
    return repetidos
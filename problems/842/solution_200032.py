def pontos_por_time(jogo):
    
    time1=0
    time2=0
    
    num1=jogo[0]
    pont1=num1[2]
    
    if pont1[0]>pont1[1]:
        time1=3
        time2=0
        
      
    
    if pont1[0]==pont1[1]:
        time1=1
        time2=1
        
        
    if pont1[0]<pont1[1]:
        time1=0
        time2=3
        
    time3=0
    time4=0
    
    num2=jogo[1]
    pont2=num2[2]
    
    if pont2[0]>pont2[1]:
        time3=3
        time4=0
        
    if pont2[0]==pont2[1]:
        time3=1
        time4=1
        
    if pont2[0]<pont2[1]:
        time3=0
        time4=3
        
        pont1=time1+ time4
        pont2= time2+ time3
        
        return {num1[0]:pont1, num1[1]:pont2}
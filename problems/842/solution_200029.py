def pontos_por_time(jogo):
    
    'Flamínthians1'=0
    'Cormengo2'=0
    
    num1=jogo[0]
    pont1=num1[2]
    
    if pont1[0]>pont1[1]:
        'Flamínthians'=3
        'Cormengo'=0
        
      
    
    if pont1[0]==pont1[1]:
        'Flamínthians1'=1
        'Cormengo2'=1
        
        
    if pont1[0]<pont1[1]:
        'Flamínthians1'=0
        'Coemengo2'=3
        
    'Flamínthians'=0
    'Cormengo'=0
    
    num2=jogo[1]
    pont2=num2[2]
    
    if pont2[0]>pont2[1]:
        'Flamínthians3'=3
        'Cormengo4'=0
        
    if pont2[0]==pont2[1]:
        'Flamínthians3'=1
        'Cormengo4'=1
        
    if pont2[0]<pont2[1]:
        'Flamínthians3'=0
        'Cormengo4'=3
        
        pont1='Flamínthians1'+ 'Flamínthians3'
        pont2= 'Cormengo2'+ 'Cormengo4'
        
        return {'Flamínthians':pont1, 'Cormengo':pont2}
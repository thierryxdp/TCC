def pontos_por_time(l1,l2):
    
    #lista1- jogo da ida
	if l1[2][0]>l1[2][1]:
        ndepontosl1[0]=3
        
    if l1[2][0]<l1[2][1]:
        ndepontosl1[1]=3
        
    if l1[2][0]==l1[2][1]:
        ndepontosl1[0]=1
        ndepontosl1[1]=1
        
    #lista2- jogo da volta
    if l2[2][0]>l2[2][1]:
        ndepontosl2[0]=3
        
    if l2[2][0]<l2[2][1]:
        ndepontosl2[1]=3
        
    if l2[2][0]==l2[2][1]:
        ndepontosl2[0]=1
        ndepontosl2[1]=1
        
    dic={l1[0]:ndepontosl1[0]+ndepontosl2[1], l1[1]:ndepontosl1[1]+ndepontosl2[0]}
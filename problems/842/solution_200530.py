def pontos_por_time(l1):
    
    #lista1- jogo da ida

    if l1[0][2][0]>l1[0][2][1]:
       l1ndepontostime1=3


    if l1[0][2][0]<l1[0][2][1]:
        l1ndepontostime2=3


    if l1[0][2][0]==l1[0][2][1]:
        l1ndepontostime1=1
        l1ndepontostime2=1
        
    #lista2- jogo da volta
    if l1[1][2][0]>l1[1][2][1]:
        l2ndepontostime2=3

    if l1[1][2][0]<l1[1][2][1]:
        l2ndepontostime1=3
    
    if l1[1][2][0]==l1[1][2][1]:
        l2ndepontostime1=1
        l2ndepontostime2=1

    dic={l1[0][0]:l1ndepontostime1+l2ndepontostime1, l1[0][1]:l1ndepontostime2+l2ndepontostime2}
    return dic
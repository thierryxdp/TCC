def pontos_por_time(lista):
    """xxxxxxx"""
    
    gols1= [x,y]
    gols2= [a,b]
    
    lis1 = [str, str, gols1]
    lis2 = [str, str, gols2]
    
   
    
    lista = [lis1, lis2]
    
    
    dicionario = {}
    
    if gols1[0] > gols1[1] and gols2[1] > gols2[0]:
        dicionario = {lis1[0]: 6, lis1[1]: 0}
    if gols1[1] > gols1[0] and gols2[0] > gols2[1]:
        dicionario = {lis1[0]: 0, lis1[1]: 6}
    if (gols1[0] > gols1[1] and gols2[0]==gols2[1]) or (gols1[0]==gols1[1] and gols2[1] > gols2[0]):
        dicionario = {lis1[0]: 4, lis1[1]: 1}
    if (gols1[1] > gols1[0] and  gols2[0]==gols2[1]) or (gols2[0]==gols2[1] and gols2[0] > gols2[1]):
        dicionario = {lis1[0]: 1, lis1[1]: 4}
    if (gols1[0] > gols1[1] and gols2[1] > gols2[0]) or (gols1[1] > gols1[0] and gols2[0] > gols2[1]):
        dicionario = {lis1[0]: 3, lis1[1]: 3}
    if gols1[0]==gols1[1] and gols2[0]==gols2[1]:
        dicionario = {lis1[0]: 2, lis1[1]: 2}
        
        return dicionarioo
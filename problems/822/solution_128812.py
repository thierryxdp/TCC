def repetidos(listNum):
    i=0
    count=0
    while i < len(listNum)-1:
        if listNum[i] == listNum[i+1]:
            count+=1
    i+=1
    return count
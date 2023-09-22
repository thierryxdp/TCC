def melhor_volta(numeros):
    melhor=[]
    cont=1
    dicts = {}
    matrix = np.zeros((6,10)) 
    for k in numeros:
        minimo = min(k)
        min_index=[]
        for i in range(0,len(k)):
          if minimo == k[i]:
            min_index.append(i)
        melhor.append([round(minimo,2),min_index[0]])
        dicts['Corredor#'+str(cont)] = round(minimo,2),min_index[0]
        cont +=1
    minval = min(dicts.values())
    res = [k for k, v in dicts.items() if v==minval]
    dicts[res[0]]  
    return res[0],dicts[res[0]]
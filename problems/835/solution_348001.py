def melhor_volta(x):
    a=[]
    for i in range(len(x)):
        a.append(min(x[i]))
    return a.index(min(a))+1,min(a),x[a.index(min(a))].index(min(a))+1
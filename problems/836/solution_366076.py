def busca(setor,matriz):
    t=0
    func=[]
    while t<len(matriz):
       if setor in matriz[t]:
           func=matriz[t]
    t+=1
    return func
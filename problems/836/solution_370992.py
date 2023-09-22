def busca(setor:str,matriz:list)->list:
    '''Função que busca na matriz, com informações dos funcionários, quais pertencem ao setor solicitado.'''
    m=[]
    ind=0
    while ind<len(matriz):
       if setor.lower() in matriz[ind][0].lower():
          m.append(matriz[ind])
          ind=ind+1
        else:
          ind=ind+1
   	return m
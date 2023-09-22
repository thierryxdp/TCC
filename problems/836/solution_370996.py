def busca(setor:str,matriz:list)->list:
    '''Função que recebe como entrada uma string referente ao setor buscado, e uma matriz com as informações dos funcionários e deve retornar uma lista de funcionários daquele setor.'''
    funcionarios=[]
    ind=0
    for i in range(len(matriz)):
        if setor.lower() in matriz[ind][0].lower():
           matriz.append(matriz[i])
           ind=ind+1
        else:
           ind=ind+1
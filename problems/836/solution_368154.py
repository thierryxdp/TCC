def busca(setor, matriz):
    for i in range(len(matriz)):
        #print(matriz[i], matriz[i][1])
        if matriz[i][1] == setor:
            return matriz[i]

        
#busca('cont',[['hele','cont','344'],['juju','adm','233']])
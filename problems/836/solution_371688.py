def busca(matriz, setor):
    ''' Entrada: matriz -> matriz com quatro entradas, representando
   				 as informações referentes a nome, registro, setor e
                 telefone de um funcionário, nesta ordem, dado do tipo list
    			 
                 setor -> nome de um setor da empresa, dado do tipo string
             
              
    	
        Saída: recebendo a matriz a função faz uma busca por setor, ou seja,
        	   dado um nome do setor da empresa, a função retorna os dados
               de tods os funcionários daquele setor'''
    contato=[]
    if setor in matriz[0]:
        contato = contato + [matriz[0]]
        contato[0].remove(setor)
        contato = contato
    if setor in matriz[1]:
        contato = contato + [matriz[1]]
        contato[0].remove(setor)
    if setor in matriz[2]:
        contato = contato + [matriz[2]]
        contato[0].remove(setor)
    return contato
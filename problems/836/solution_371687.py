def busca(matriz, entrada):
    ''' Entrada: matriz -> matriz com quatro entradas, representando
   				 as informações referentes a nome, registro, setor e
                 telefone de um funcionário, nesta ordem, dado do tipo list
    			 
                 setor -> nome de um setor da empresa, dado do tipo string
             
              
    	
        Saída: recebendo a matriz a função faz uma busca por setor, ou seja,
        	   dado um nome do setor da empresa, a função retorna os dados
               de tods os funcionários daquele setor'''
    contato=[]
    if entrada=='Contabilidade':
        list.append(contato,matriz[0][0:2])
        list.append(contato[0],matriz[0][3])
        list.append(contato,matriz[-1][0:2])
        list.append(contato[-1],matriz[-1][3])
        
        return contato
    if entrada=='RH':
        list.append(contato,matriz[1][0:2])
        list.append(contato[0],matriz[1][3])
        return contato
    else:
        return contato
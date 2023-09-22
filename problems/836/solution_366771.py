def busca(setor,M):
    """Recebe como entrada dois argumentos: Matriz e setor.
    A matriz possuindo strings contendo
    as informações dos funcionários de uma empresa, na qual são 
    fornecidos o nome,o registro, o setor e o número de telefone.
    A função retorna as informações de contato do funcionário do setor
    especificado.Caso não haja registro, a função deverá retornar uma lista
    vazia.
    Exemplo: 
    >>>busca("RH",matriz)
    >>>[["JulianaVasconcelos"","465","(21)3555-4552"]]
    
    list(list(str))->list(list)
  
    """
    lista=[]
    linhas=range(len(M))
    for i in linhas:
        if M[i][2]== setor:
            list.append(lista,[M[i][0],M[i][1],M[i][3]])
    return lista
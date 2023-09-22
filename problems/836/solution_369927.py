# QUESTÃO 5 - OK!
def busca(s,m):
    """ Dado uma matriz (nome,registro,setor,telefone) e um setor vamos retormar o(s) funcionario(s) que trabalham nesse setor.
        Parametros:
        Entrada -> matriz : list
        Saida   -> list   """
    lista=[]
    num_linha=len(m)
    num_coluna=len(m[0])

    for i in range(num_linha):
        lista1=[]
        if s in m[i][2]:
            nome=m[i][0]
            registro=m[i][1]
            tel=m[i][3]
            list.append(lista1,nome)
            list.append(lista1,registro)
            list.append(lista1,tel)
            list.append(lista,lista1)
    return lista




    
        




m = [ ['Adalberto Ferreira','556','Contabilidade','(21)84564-5248']
      ,['Juliana Vasconcelos','465','RH','(21)3555-4552]']
      ,['Flavia Amorim','565','Contabilidade','(21)2134-4845'] ]
busca('RH',m)
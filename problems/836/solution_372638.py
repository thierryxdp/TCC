def busca(setor: str, funcionarios: list[list[str]]) -> list[list[str]]:
   '''Retorna todos os funcionários na lista funcionarios que trabalham no
      setor dado'''
   #Criando lista de retorno
   listaR = []
   for ele in funcionarios:
      if ele[2] == setor:
         ele = list.pop(ele,2)
         listaR.append(ele)

   return listaR
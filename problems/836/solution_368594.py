def busca(setor, matriz):
     '''Funcao que, dado um setor e uma matriz, retornaos dados de todos os funcionarios daquele setor.
    str, matriz -> str'''
     lista=[]
     for informacoes in matriz:
         if str.lower(setor) == str.lower(informacoes[2]):
             list.append(lista, [informacoes[0], informacoes[1], informacoes[3]])
         else:
              return('\nNenhum registro encontrado.')
     
     return lista
def busca(setor,dados):
    """Função que dado o nome de um setor da empresa, retorna a lista com
       os dados do funcionario que trabalha naquele setor(ou uma lista
       vazia caso ninguém trabalhe naquele setor).
       str,list -> list

       Parâmetros:
       setor: O setor que o(s) funcionario(s) trabalham que se deseja 
              separar e avaliar as informações de quem trabalha lá 
       dados: Uma lista com os dados dos funcionarios existentes no
              armazenamento da empresa.

       Returns: Uma lista com os dados do funcionario que trabalha
                naquele setor(ou uma lista vazia caso ninguém trabalhe
                naquele setor).
    """
    informacoes = []
    for funcionarios in dados:
        if setor in dados[2]:
            informacoes += [funcionarios[0],funcionarios[1],funcionarios[3]]
    return informacoes
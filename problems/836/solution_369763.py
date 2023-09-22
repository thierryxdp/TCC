#Entrada: O nome de um setor e uma matriz
#1)Precisamos buscar em cada linha da matriz qual funcionário
#1.1)Trabalha naquele setor
#2)Ao encontrar, adicionaremos os dados desse funcionario em uma lista
#3)Ao final, retornaremos essa lista, que contém os dados de todos
#3.1)Os funcionarios encontrador

def busca(setor:str,funcionarios:list)->list:
    lista=[]
    for funcionario in funcionarios:
        if (funcionario[2] == setor):
            funcionario.pop(2)
            lista.append(funcionario)
    return lista
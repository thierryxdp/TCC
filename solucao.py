def concatenacao(a, b):
    a = str(a)
    b = str(b)
    return a+b+b+a

def concatenacao_com_tipo(a: str, b: str) -> str:
    a = str(a)
    b = str(b)
    return a+b+b+a

def concatenacao2(a, b):
    return a + b + b + a

def concatenacao2_com_tipo(a: str, b: str) -> str:
    return a + b + b + a

def concatenacao3(a, b):
    return a[:len(a)//2] + b + a[len(a)//2:]

def concatenacao3_com_tipo(a: str, b: str) -> str:
    return a[:len(a)//2] + b + a[len(a)//2:]

def concatenacao4(a, b):
    return "a"+"b" + "b"+"a"

def concatenacao4_com_tipo(a: str, b: str) -> str:
    return "a"+"b" + "b"+"a"


def busca(setor,matriz):
    '''funcao que dado o nome de um setor da empresa, retorna os dados de todos os funcionarios daquele setor
    matriz->lista'''
    result = []
    for line in matriz:
        if (line[2] == setor):
            result.append(line[0:2] + [line[3]])
    
    if(len(result) == 0):
        return "Nenhum registro encontrado"
    
    return result

def busca_com_tipo(setor: str, matriz: list[list]) -> list[list]:
    '''funcao que dado o nome de um setor da empresa, retorna os dados de todos os funcionarios daquele setor
    matriz->lista'''
    result = []
    for line in matriz:
        if (line[2] == setor):
            result.append(line[0:2] + [line[3]])
    
    if(len(result) == 0):
        return "Nenhum registro encontrado"
    
    return result

def diff_datas_com_tipo(data1: str, data2:str) -> int:
    return 365*(int(data2[6:10]) - int(data1[6:10])) + 30*(int(data2[3:5]) - int(data1[3:5])) + int(data2[0:2]) - int(data1[0:2])
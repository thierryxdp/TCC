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
    listaresultados=[]
    for i in range(len(matriz)):
                   for j in range(len(matriz[i])):
                        if matriz[i][2]==setor:
                            listaresultados.append(matriz[i])
    return listaresultados

def busca_com_tipo(setor: str, matriz: list[list]) -> list[list]:
    '''funcao que dado o nome de um setor da empresa, retorna os dados de todos os funcionarios daquele setor
    matriz->lista'''
    listaresultados=[]
    for i in range(len(matriz)):
                   for j in range(len(matriz[i])):
                        if matriz[i][2]==setor:
                            listaresultados.append(matriz[i])
    return listaresultados
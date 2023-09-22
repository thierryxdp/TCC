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
def soma(produtos):
    som = 0
    for k,v in produtos.items():
        som += v
    return som
prd = { 
        "farinha": 13.85,
        "melancia": 15.21,
        "farinha": 5.23
        }
print(soma(prd))
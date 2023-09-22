def num_bombons():
    preco_bombom = float(input("qual o preço do bombom"))
    dinheiro_pedrinho = float(input("quanto dinheiro pedrinho tem"))
    return int(dinheiro_pedrinho/preco_bombom)
print(num_bombons())
# Verifica se o colchão passa ou não na porta do joao
# Altura H Largura L
def colchao(medidas,H,L):
    Medidas->Lista com tamanhos inteiros A,B e C
    H->ALTURA
    L->Largura
    tamanho = H*L
    if medidas<tamanho:
        return True
    else:
        return False
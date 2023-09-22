"""Retorna se o colchão passa ou não pela porta"""
def colchao(medidas,H,L):
	medidas=[A,B,C]
    if medidas>H:
        return False
    if medidas<L:
        return True
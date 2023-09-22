"""Retorna se o colchão passa ou não pela porta"""
def colchao(medidas,H,L):
    if int(medidas>H):
        return False
    if medidas<L:
        return True
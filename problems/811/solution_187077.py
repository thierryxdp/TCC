"""Retorna se o colchão passa ou não pela porta"""
def colchao(medidas,H,L):
	[A,B,C]=medidas
    if medidas>H:
        return False
    if medidas<L:
        return True
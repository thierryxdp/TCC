# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     """Recebe os 2 primeiros valores em str e i para
     o número da posição a ser trocada e concatena;
     str, str, int -> str"""
        if i<len(s) and i<=0:
            return s[:i] + x + s[i+1:]
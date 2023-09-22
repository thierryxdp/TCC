# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função de substituição; input: string, int, int. return: string"""
    
    if i <= len(s):
        return s[:i]+x+s[i+1:]
    
    else:
        return 0
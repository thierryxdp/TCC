# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string s, exceto que o elemento na posição i estará substiuído por x
   Testes substitui('cana','m',3) == 'cama'
   substitui('cauda','l',3) == calda
   Assinatura: str, str, int --> str
    """
    pedaco = s[0:i]
    return pedaco - s[i] + x
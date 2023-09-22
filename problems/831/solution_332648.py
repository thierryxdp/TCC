def lingua_p(s):
    """Função que recebe uma palara em português qualquer e retorna ela na línngua o P
assinatura: string -> string
testes:
lingua_p("computação") == 'copompuputapaçãopo'
lingua_p("Victor") == 'vipictopor'
lingua_p("Física") == 'fípísipicapa'
"""
    p = s.lower()
    p = str.replace(p,"a","apa")
    p = str.replace(p,"e","epe")
    p = str.replace(p,"i","ipi")
    p = str.replace(p,"o","opo")
    p = str.replace(p,"u","upu")
    p = str.replace(p,"á","ápá")
    p = str.replace(p,"é","épé")
    p = str.replace(p,"í","ípí")
    p = str.replace(p,"ó","ópó")
    p = str.replace(p,"ú","úpú")
    return p
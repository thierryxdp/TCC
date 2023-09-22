def lingua_p(palavra):
    traducao=''
    palavra=str.lower(palavra)
    retira='qwrtypsdfghjklçzxcvbnm'
    for i in range(len(palavra)):
        if palavra[i] not in retira:
            traducao+=palavra[i]+'p'+palavra[i]
        else:
            traducao+=palavra[i]
        return traducao
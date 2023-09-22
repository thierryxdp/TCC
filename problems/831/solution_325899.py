def lingua_p(palavra):
    traducao=''
    palavra=str.lower(palavra)
    retira='bcdfghjklmnpqrstvwxyzç'
    for x in range(len(palavra)):
        if palavra[x] not in retira:
            traducao+=palavra[x]+'p'+palavra[x]
        else:
            traducao+=palavra[x]
        return traducao
def lingua_p(palavra):
    traducao=""
    palavra=str.lower(palavra)
    restricao="qwrtypsdfghjklçzxcvbnm"
    for i in range(len(palavra)):
        if palavra[i] not in restricao:
            traducao+=palavra[i]+"p"+palavra[i]
        else:
             traducao+=palavra[i]
            	return traducao
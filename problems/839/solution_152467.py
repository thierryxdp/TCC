def carros (num_pess,capac=5):
    return round((num_pess/capac)+((num_pess%capac)/(capac-1)))
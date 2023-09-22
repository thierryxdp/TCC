def filtra_pares(nume,numi,numu,numo):
    if nume % 2:
        return nume
    if numi % 2:
        return numi
    if numu % 2:
        return numu
    if numo % 2:
        return numo
    return [nume,numi,numo,numu]
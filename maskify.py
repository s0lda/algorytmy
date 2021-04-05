def maskify(cc):
    # last 4 digits will remain visible
    mask = '#'*(len(cc)-4)
    return mask + cc[-4:]

def spell(txt):
    n = len(txt)
    if n:
        print(txt[-1])
    if 1 < n:
        spell(txt[:-1])

txt = input()
spell(txt)

# Решение за N*M с маленьким багом
''' def strcounter(stroka):
    for sym in stroka:
        counter = 0
        for sub_sym in stroka:
            if sub_sym == sym:
                counter += 1
        print(sym,counter)

strcounter('aabcbd') '''

# Решение за N*M, где M = N => N**2
''' def strcounter(stroka):
    for sym in set(stroka):
        counter = 0
        for sub_sym in stroka:
            if sub_sym == sym:
                counter += 1
        print(sym,counter)

strcounter('aabcbd') '''

# Решение за N
def strcounter(stroka):
    syms_counter = {}
    for sym in stroka:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(syms_counter)

strcounter('aabcbd')
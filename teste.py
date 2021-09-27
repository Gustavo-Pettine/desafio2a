from tc.glc import *

V = {'S'}
T = {'0', '1'}
P = {
    ('S', ()),
    ('S', (2)),
    ('S', (1)),
    ('S', (2, 'S', 2)),
    ('S', (1, 'S', 1)),
}

modelo = (V, T, P, 'S')

print(lmd(modelo, 1))
print(lmd(modelo, 2))
print(lmd(modelo, 11))
print(lmd(modelo, 22))
print(lmd(modelo, 212))
print(lmd(modelo, 121))
print(lmd(modelo, 22122))
print(lmd(modelo, 11211))
print(lmd(modelo, 112211))
print(lmd(modelo, 221122))

print()

print(lmd(modelo, 112212211))
print(lmd(modelo, 212212212))
print(lmd(modelo, 122212221))
print(lmd(modelo, 221121122))
print(lmd(modelo, 121121121))
print(lmd(modelo, 211121112))
print(lmd(modelo, 22111211122))
print(lmd(modelo, 21111211112))
print(lmd(modelo, 21211211212))
print(lmd(modelo, 21221212212))

print()

print(lmd(modelo, 11221212211))
print(lmd(modelo, 11222222211))
print(lmd(modelo, 11121212111))
print(lmd(modelo, 2212212122122))
print(lmd(modelo, 2112212122112))
print(lmd(modelo, 2111212121112))
print(lmd(modelo, 2111112111112))
print(lmd(modelo, 1222221222221))
print(lmd(modelo, 1212221222121))
print(lmd(modelo, 1212121212121))

print()

print(lmd(modelo, 212121212121212))
print(lmd(modelo, 222121212121222))
print(lmd(modelo, 221121212121122))
print(lmd(modelo, 222121111121222))
print(lmd(modelo, 11221211111212211))
print(lmd(modelo, 12221212121212221))
print(lmd(modelo, 2122212121212122212))
print(lmd(modelo, 2122112121212112212))
print(lmd(modelo, 2122112221222112212))
print(lmd(modelo, 2121112121212111212))
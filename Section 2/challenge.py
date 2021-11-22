# Coding challenge part 1
# Interest calculator

p = input('Princible (P)? ')
n = input('Number of years? ')
r = input('Interest rate? ')

p = int(p)
n = int(n)
r = int(r)

si = (p * n * r) / 100

print(si)
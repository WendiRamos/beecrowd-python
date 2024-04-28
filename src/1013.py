valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maior_ab = (a + b + abs(a - b)) / 2

maior_bc = (b + c + abs(b - c)) / 2

maior_abc = (maior_ab + maior_bc + abs(maior_ab - maior_bc)) / 2

print(f"{int(maior_abc)} eh o maior")

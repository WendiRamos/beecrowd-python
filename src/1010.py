entrada_1 = input()
entrada_2 = input()

valores_1 = entrada_1.split()
valores_2 = entrada_2.split()

quantidade_1 = int(valores_1[1])
valor_1 = float(valores_1[2])

quantidade_2 = int(valores_2[1])
valor_2 = float(valores_2[2])

soma = quantidade_1 * valor_1 + quantidade_2 * valor_2

print(f"VALOR A PAGAR: R$ {soma:.2f}")

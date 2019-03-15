vetS = []

n = int(input("Digite o tamanho do vetor: "))

for i in range (0, n):
    elem = int (input("Digite o elemento: "))
    vetS.append(elem)

vetS.reverse()

print(vetS)

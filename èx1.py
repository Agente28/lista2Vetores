vetA = []

n = int(input("Digite o Tamanho do vetor: "))

for i in range(0, n):
    elem = int(input("Digite o elemento: "))
    vetA.append(elem)

x = int(input("Digite um elemento pra busca: "))

for j in range(0, n):
    if(vetA[j] == x):
        print("Valor encontrado!")



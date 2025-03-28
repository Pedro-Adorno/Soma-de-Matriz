linhas_a = int(input('Quantidade de linhas: '))
colunas_a = int(input('Quantidade de colunas: '))

matriz_a = []
for i in range(linhas_a):
    linha = []        
    for j in range(colunas_a):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz_a.append(linha)
    
print("Matriz A:")
for linha in matriz_a:
    print(linha)


linhas_b = int(input('Quantidade de linhas: '))
colunas_b = int(input('Quantidade de colunas: '))

matriz_b = []

for i in range(linhas_b):
    linha = []        
    for j in range(colunas_b):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz_b.append(linha)

print("Matriz B:")    
for linha in matriz_b:    
    print(linha)
if linhas_a != linhas_b or colunas_a != colunas_b:
    print('As matrizes não possuem as mesmas dimensões e não podem ser somadas!')
else:
    matriz_c = []

    for i in range(linhas_a):
        linha = []
        for j in range(colunas_a):
            soma = matriz_a[i][j] + matriz_b[i][j]
            linha.append(soma)
        matriz_c.append(linha)

    print("Matriz C:")
    for linha in matriz_c:        
            print(linha)

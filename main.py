## 1) Operações Básicas com Listas

print("\n-- 1) OPERAÇOES BÁSICAS COM LISTAS --\n")

frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
numeros = [10, 25, 3, 47, 8, 15, 30]
print(f"Sem negativo: Primeiro = {frutas[0]}, Último = {frutas[len(frutas)-1]}")
print(f"Com negativo: Primeiro = {frutas[-5]}, Último = {frutas[-1]}")

frutas.append('morango')
frutas.insert(2, 'kiwi')

frutas.remove('banana')
print("Lista frutas modificada:", frutas)

print("Números maiores que 15:")
for num in numeros:
    if num > 15:
        print(num, end=" ")
print()

print("Crescente:", sorted(numeros))
print("Decrescente:", sorted(numeros, reverse=True))
print("Original mantida:", numeros)

## 2)  Fatiamento (Slicing) de Listas

print("\n-- 2) FATIAMENTO(SLICING) DE LISTAS --\n")

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print("1.", letras[:4])

print("2.", letras[2:7])

print("3.", letras[-3:])

print("4.", letras[::-1])

print("5.", letras[::2])

## 3) List Comprehension

print("\n-- 3) LIST COMPREHENSION --\n")


palavras = ['python', 'lista', 'programação', 'código', 'loop', 'função']
numeros = list(range(1, 21))

quadrados = [x**2 for x in range(1, 11)]
print("1.", quadrados)

pares = [x for x in numeros if x % 2 == 0]
print("2.", pares)

tamanhos = [len(p) for p in palavras]
print("3.", tamanhos)

longas_maiusculas = [p.upper() for p in palavras if len(p) > 5]
print("4.", longas_maiusculas)

tuplas_quadrados = [(x, x**2) for x in range(1, 6)]
print("5.", tuplas_quadrados)

## 4) Funções Úteis de Listas

print("\n-- 4) FUNÇOES ÚTEIS DE LISTAS --\n")

notas = [7.5, 8.0, 6.0, 9.5, 5.5, 8.5, 7.0, 9.0, 6.5, 8.0]
nomes = ['Carlos', 'Ana', 'Bruno', 'Ana', 'Diego', 'Ana', 'Bruno']

media = sum(notas) / len(notas)
print(f"1. Média das notas: {media:.2f}")

maior_nota = max(notas)
menor_nota = min(notas)
acima_da_media = len([n for n in notas if n > media])
print(f"2. Maior: {maior_nota} | Menor: {menor_nota} | Acima da média: {acima_da_media}")

print(f"3. Ocorrências de Ana: {nomes.count('Ana')}")

print(f"4. Índice do Bruno: {nomes.index('Bruno')}")

nomes_unicos = []
for nome in nomes:
    if nome not in nomes_unicos:
        nomes_unicos.append(nome)
print("5. Nomes sem repetição:", nomes_unicos)

## 5) Lista sem repetição mantendo a ordem original

print("\n-- 5) LISTA SEM REPETIÇAO MANTENDO A ORDEM ORIGINAL --\n")

turma = [
    ['Alice', 8.0, 7.5, 9.0],
    ['Bruno', 6.5, 7.0, 8.0],
    ['Carla', 9.5, 9.0, 9.5],
    ['Diego', 5.0, 6.0, 5.5],
    ['Elena', 7.0, 8.5, 7.5],
]

medias_alunos = []
for aluno in turma:
    nome = aluno[0]
    media_individual = sum(aluno[1:]) / 3
    medias_alunos.append([nome, media_individual])
    print(f"Aluno: {nome} | Média: {media_individual:.2f}")

melhor_aluno = max(medias_alunos, key=lambda x: x[1])
print(f"\n2. Maior média: {melhor_aluno[0]} ({melhor_aluno[1]:.2f})")

aprovados = [a[0] for a in medias_alunos if a[1] >= 6.0]
reprovados = [a[0] for a in medias_alunos if a[1] < 6.0]
print(f"3. Aprovados: {aprovados} | Reprovados: {reprovados}")

media_geral = sum([a[1] for a in medias_alunos]) / len(medias_alunos)
print(f"4. Média geral da turma: {media_geral:.2f}")

turma.append(['Felipe', 8.0, 7.5, 8.5])

ranking_atualizado = []
for aluno in turma:
    nome = aluno[0]
    media_ind = sum(aluno[1:]) / 3
    ranking_atualizado.append((nome, media_ind))

ranking_ordenado = sorted(ranking_atualizado, key=lambda x: x[1], reverse=True)

print("\n5. Ranking da Turma (Decrescente):")
for posicao, (nome, med) in enumerate(ranking_ordenado, start=1):
    print(f"{posicao}º - {nome}: {med:.2f}")
def calcular_media(nota1, nota2, total_notas):
  return (nota1 + nota2) / total_notas

total_notas = 2
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2, total_notas)
print(f" Média : {media:.2f}")
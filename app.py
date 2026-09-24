# projeto Exemplo: calculadora de Média do aluno
def calcular_media(nota1, nota2):
   return (nota1 + nota2) /2

print("=================================")
print("=== Sistema de Notas do Aluno ===")
print("=================================")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = calcular_media(n1, n2)
print(f"A média final é: {media:.2f}")

if media >= 7.0:
   print("Status: APROVADO!")

elif media >= 5.0:
   print("Status: Recuperação.")

else:
   print("Status: Reprovado.")
print("=================================")
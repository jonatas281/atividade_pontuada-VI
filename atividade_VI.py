import os 
os . system ("cls || clear")

# declarando variaveis
dados=[]
soma_salario=0
quantidade_mulheres_acima_5000=0

def adicionar_pessoas():
    global soma_salarios, quantidade_mulheres_acima_5000
idade = int(input("digite sua idade: "))
sexo = input("digite o sexo (M|F): ").strip().upper()
salario = float(input("digite seu salario:"))
dados.append((idade,sexo,salario))

soma_salario += salario
    
 
if sexo == 'F' and salario >= 5000:
        quantidade_mulheres_acima_5000 += 1

def exibir_resultados():
    if not dados:
        print("Nenhum dado foi registrado.")
        return

    while True:
        print(""""
             Menu
        1 - Adicionar pessoa
        2 - Exibir resultados e sair    """)


        opcao = input("Escolha uma opção: ")

        match opcao :
             case 1 :
                  print("adicionar pessoa")
             case 2 :
                  print("exibir resultado")
             case _ :
                   break
    
    print("Opção inválida. Tente novamente.")
    media_salario = soma_salarios / len(dados)

    # Cálculo da maior e menor idade
    idades = [idade for idade,sexo,salario in dados]
    maior_idade = max(idades)
    menor_idade = min(idades)

    # Exibe os resultados
    print(f"Média de salário do grupo: R$ {media_salario:.2f}")
    print(f"Maior idade do grupo: {maior_idade} anos")
    print(f"Menor idade do grupo: {menor_idade} anos")
    print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres_acima_5000}")

    
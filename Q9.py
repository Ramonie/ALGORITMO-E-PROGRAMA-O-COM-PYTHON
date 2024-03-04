print("9. Calcule o preço médio do quilômetro rodado (R$/km) para uma dada"
"distância percorrida (km), um certo volume de combustível gasto (litro) e o"
"preço do combustível (R$/litro).")
inicio = int(input("Digite a quilometragem inicial do seu veiculo:  "))
final = int(input("Digite a quilometragem final da sua viagem:   "))
kmviagem = final - inicio
litros = int(input("Seu veiculo faz quantos quilometros com 1 Litro de combustivel:  "))
Valor_Litro = float(input("Digite o valor em reais por litro de combustivel:  "))
media = kmviagem/litros
Custo_Comb = (media*Valor_Litro)
Custo_Km = float(Custo_Comb/kmviagem)
print("Seu custo por quilometro rodado foi: R$",+Custo_Km)


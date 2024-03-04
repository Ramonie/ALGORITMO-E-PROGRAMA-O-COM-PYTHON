print("Dado a idade de uma pessoa em anos, meses e dias, encontrar a idade aproximada dessa pessoa em dias.")
anos = int(input("Digite sua idade em ANOS:  "))
meses = int(input("Se, sua idade for: EX(18 anos e 3 meses), por favor digitar o núemro de meses:  "))
dias = int(input("Se sua idade for em anos, meses e dias, por favor digitar o número de dias:  "))
multanos = anos * 365
multmeses = meses * 30
idade =int(multanos+multmeses+dias) 
print("Sua idade expressa em dias:",+idade,"dias ")

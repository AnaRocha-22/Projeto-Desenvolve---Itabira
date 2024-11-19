juros = 0.01  
saldo = 500.0
saldo += saldo * juros  # Após o primeiro mês
saldo += saldo * juros  # Após o segundo mês
saldo += saldo * juros  # Após o terceiro mês
print("Após 3 meses meu novo saldo é R$")
print(round(saldo)) # round usada para arredondar um número
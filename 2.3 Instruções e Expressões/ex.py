# Definição das variáveis
salario_por_hora = 20.0
horas_trabalhadas = 40

# Cálculo do salário bruto
salario_bruto = salario_por_hora * horas_trabalhadas

# Cálculo dos descontos
desconto_inss = salario_bruto * 0.10
desconto_sindicato = salario_bruto * 0.05

descontos_totais = desconto_inss + desconto_sindicato

# Cálculo do salário líquido
salario_liquido = salario_bruto - descontos_totais

# Exibição dos resultados
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (10%): R$ {desconto_inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

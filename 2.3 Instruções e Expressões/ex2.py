# Definição das variáveis
salario_por_hora = 20.0
horas_trabalhadas = 40

# Cálculo do salário bruto
salario_bruto = salario_por_hora * horas_trabalhadas

# Cálculo do salário líquido em uma única expressão
salario_liquido = salario_bruto - (salario_bruto * 0.10 + salario_bruto * 0.05)

# Exibição dos resultados
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
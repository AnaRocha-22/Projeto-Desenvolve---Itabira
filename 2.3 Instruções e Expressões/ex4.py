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

# Conversão de moeda
quantia_brl = 100  # Defina o valor em reais
cambio_brl_para_cny = 0.69
quantia_cny = quantia_brl / cambio_brl_para_cny

# Exibição do valor convertido
print(f"{quantia_brl:.2f} BRL equivale a {quantia_cny:.2f} CNY")

# Cálculo da velocidade média para a Maratona Internacional de São Silvestre
distancia_km = 42.195  # Distância em quilômetros
tempo_horas = 3  # Tempo em horas

distancia_metros = distancia_km * 1000  # Convertendo para metros
tempo_segundos = tempo_horas * 3600  # Convertendo para segundos

velocidade_media = distancia_metros / tempo_segundos  # Velocidade média em m/s

# Exibição do resultado
print(f"Velocidade média necessária: {velocidade_media:.2f} m/s")

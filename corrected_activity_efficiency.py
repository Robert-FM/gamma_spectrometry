import math

# Entrada de dados
a = float(input('Digite a atividade inicial (Bq): '))
t_transcorrido = float(input('Digite o valor do tempo: '))
t_meia = float(input('Digite o tempo de meia-vida: '))
area = float(input('Digite o valor da área do fotopico (u.a.): '))
gamao = float(input('Digite o valor da probabilidade de emissão: '))
tempo_analise = float(input('Digite o valor do tempo de análise (s): '))

# Cálculo da constante de decaimento e atividade final
cte_lambda = math.log(2) / t_meia
a_f = a * math.exp(-cte_lambda * t_transcorrido)

# Exibe a atividade corrigida
print(f'A atividade corrigida é {a_f:.2f} Bq.')

# Cálculo da eficiência
e = area / (a_f * gamao * tempo_analise)

# Exibe a eficiência calculada
print(f'O valor da eficiência é de {e:.3f}.')

#https://pt.calcuworld.com/calendarios/calculadora-de-tempo-entre-duas-datas/
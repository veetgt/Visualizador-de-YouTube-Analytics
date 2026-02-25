import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("content/Dados da tabela.csv")

df['Duração média da visualização'] = pd.to_timedelta(df['Duração média da visualização']).dt.total_seconds()

# Converte "Duração média da visualização" para segundos
df['Duração média da visualização'] = pd.to_timedelta(df['Duração média da visualização']).dt.total_seconds()

# Selecione as colunas relevantes para a análise de correlação.
correlation_data = df[['Visualizações', 'Tempo de exibição (horas)', 'Inscritos', 'Duração média da visualização', 'Impressões', 'Taxa de cliques de impressões (%)']]

# Matriz de correlação computacional
corr_matrix = correlation_data.corr()

# Apresentação
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Mapa de calor de correlação do YouTube Analytics")
plt.show()
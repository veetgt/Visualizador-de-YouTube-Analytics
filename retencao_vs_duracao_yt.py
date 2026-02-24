import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("content/Dados da tabela.csv")

# Converte para segundos
df['Duração média da visualização'] = pd.to_timedelta(df['Duração média da visualização']).dt.total_seconds()

# Calcula a taxa de retenção 
df['Taxa de Retenção (%)'] = (df['Duração média da visualização'] / df['Duração']) * 100

# Apresentação
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

sns.scatterplot(data=df, x='Duração', y='Taxa de Retenção (%)', hue='Visualizações', size='Visualizações', sizes=(100, 200), palette='coolwarm')
plt.title("Audience Retention vs. Video Duration")
plt.xlabel("Video Duration (seconds)")
plt.ylabel("Retention Rate (%)")
plt.legend(title="Visualizações", loc="upper right")

plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

df = pd.read_csv("content/Dados da tabela.csv")

df['Duração média da visualização'] = pd.to_timedelta(df['Duração média da visualização']).dt.total_seconds()

# Calcula a taxa de retenção 
df['Taxa de Retenção (%)'] = (df['Duração média da visualização'] / df['Duração']) * 100

# Organiza os vídeos pela taxa de retenção
df_sorted = df.sort_values(by='Taxa de Retenção (%)', ascending=False)

# Apresenta os 10 vídeos com maior retenção
df_sorted[['Título do vídeo', 'Duração', 'Duração média da visualização', 'Taxa de Retenção (%)']].head(10)

display(df_sorted.head(10))
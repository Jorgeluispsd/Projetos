import pandas as pd
import matplotlib.pyplot as plt  #Biblioteca para visualização de dados/Graficos

'''dados = pd.DataFrame({
    'Ano': ['2020', '2021', '2022', '2023'],
    'Vendas': [1500, 2000, 2500, 3000],})

print(dados)

dados.plot(x='Ano', y='Vendas', kind='bar', title='Vendas Anuais')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.show()'''


df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSSacsreDuZ3rGEn0ApUrcdSq7Swfz8SRiEJGaHOFihUa_MIwjESYE8UQoDd8kUL8N372FmVX2UtAdU/pub?gid=0&single=true&output=csv')

print('Tabela com a media de presença de alunos em uma turma com 30 alunos')
df['Media Presença'] = df['Media Presença'].str.replace(',', '.', regex=False) # Substitui vírgulas por pontos
df['Media Presença'] = pd.to_numeric(df['Media Presença'], errors='coerce') # Converte para numérico, forçando erros a NaN
df['Media Presença'] = df['Media Presença'].round(0).astype('Int64') # Arredonda e converte para inteiro, mantendo NaN se houver
print(df)


df.plot(x='Mês', y='Media Presença', kind='bar', title='Média de Presença Anual')
plt.xlabel('Mês')
plt.ylabel('Media Presença')
plt.show()
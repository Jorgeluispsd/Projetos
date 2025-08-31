import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRV7v_md9HjVmIe-xjlETJNcE6_zk9EmJWT-MU6CXpGgOPoa6BCSrxMq9mLxXXzh11WPuVjS1zZY6bQ/pub?gid=0&single=true&output=csv')

print('Tabela com a quantidade de demissões em uma empresa ao longo dos anos')
print(df)

df.plot(x='Ano', y=['Contratações', 'Demissões', 'Saldo'], kind='bar')

ax = df.plot(x='Ano', y=['Contratações', 'Demissões', 'Saldo'], kind='bar')

# Para cada grupo de barras
for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # deslocamento em pixels
                    textcoords="offset points",
                    ha='center', va='bottom')

plt.xlabel('Ano')
plt.ylabel('Quantidade')    
plt.title('Contratações, Demissões e Saldo por Ano')
plt.legend(['Contratações', 'Demissões', 'Saldo'])
plt.tight_layout()
plt.show()
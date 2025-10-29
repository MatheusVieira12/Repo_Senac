import pandas as pd
import matplotlib.pyplot as plt


meso = [40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 55, 52, 53, 51, 50, 48, 47, 46, 44, 42, 40]

lepto = [ 45, 46, 47, 48, 49, 50, 50, 49, 48, 47, 46, 45 ,45]

plati = [45, 46, 47, 48, 49, 50, 49, 48, 48, 47, 46, 45]


df_meso = pd.DataFrame({'valores': meso})
df_lepto = pd.DataFrame({'valores': lepto})
df_plati = pd.DataFrame({'valores': plati})

assimetria_meso = df_meso['valores'].skew()
curtose_meso = df_meso['valores'].kurtosis()
assimetria_lepto = df_lepto['valores'].skew()
curtose_lepto = df_lepto['valores'].kurtosis()
assimetria_plati = df_plati['valores'].skew()
curtose_plati = df_plati['valores'].kurtosis()

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(df_meso.index, df_meso['valores'], marker='o', color='red')
plt.title(f'Mesocúrtica, {(curtose_meso * 100):.2f}')
plt.xlabel('Índice')
plt.ylabel('Valores')


plt.subplot(1, 3, 2)
plt.plot(df_lepto.index, df_lepto['valores'], marker='o', color='blue')
plt.title(f'Leptocúrtica, {(curtose_lepto * 100):.2f}')
plt.xlabel('Índice')
plt.ylabel('Valores')

plt.subplot(1, 3, 3)
plt.plot(df_plati.index, df_plati['valores'], marker='o', color='green')
plt.title(f'Platicúrtica, {(curtose_plati * 100):.2f}')
plt.xlabel('Índice')
plt.ylabel('Valores')

plt.show()
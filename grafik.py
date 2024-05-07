import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Penumpang Kapal Titanic')
df = pd.read_csv('titanic.csv')

survival_count = df['survived'].value_counts()

fig_pie, ax_pie = plt.subplots(figsize=(8, 6))
ax_pie.pie(survival_count, labels=['Meninggal', 'Selamat'], autopct='%1.1f%%', startangle=90)
ax_pie.set_title('Persentase Penumpang yang Meninggal dan Selamat')
st.pyplot(fig_pie)

survival_by_sex = df.groupby(['survived', 'sex']).size().unstack()
fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
survival_by_sex.plot(kind='bar', stacked=True, ax=ax_bar)
ax_bar.set_title('Jumlah Penumpang yang Selamat dan Meninggal berdasarkan Jenis Kelamin')
ax_bar.set_xlabel('Status')
ax_bar.set_ylabel('Jumlah Penumpang')
ax_bar.set_xticklabels(['Meninggal', 'Selamat'], rotation=0)
ax_bar.legend(title='Jenis Kelamin')
st.pyplot(fig_bar)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv("bike_sharing_day.csv")
df_hour = pd.read_csv("bike_sharing_hour.csv")

# Mapping angka musim ke nama musim sebenarnya
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df_day["season"] = df_day["season"].map(season_mapping)

# Set title
st.title("📊 Bike Sharing Dashboard")

# Sidebar untuk filter
st.sidebar.header("🔍 Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", df_day['season'].unique())

# Menampilkan informasi kontak di bawah filter
st.sidebar.markdown("---")
st.sidebar.header("📩 Kontak")
st.sidebar.write("**Nama:** Revo Pratama")
st.sidebar.write("**ID Dicoding:** MC19D5Y1619")
st.sidebar.write("**Email:** revopratama2004@gmail.com")

# Filter data berdasarkan musim
filtered_df = df_day[df_day['season'] == selected_season]

# Statistik ringkasan
st.subheader("📈 Statistik Data Harian")
st.write(filtered_df.describe())

# Visualisasi jumlah penyewaan sepeda berdasarkan musim
st.subheader("🚲 Jumlah Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x=df_day["season"], y=df_day["cnt"], estimator=sum, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi jumlah penyewaan sepeda berdasarkan hari kerja vs akhir pekan
st.subheader("🗓️ Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots()
sns.barplot(x=df_day["workingday"], y=df_day["cnt"], estimator=sum, palette="coolwarm", ax=ax)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Akhir Pekan / Libur", "Hari Kerja"])
ax.set_xlabel("Kategori Hari")
ax.set_ylabel("Total Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi jumlah penyewaan sepeda berdasarkan jam
st.subheader("⏰ Jumlah Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_hour, x="hr", y="cnt", ci=None, estimator=sum, color="blue", marker="o", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Total Penyewaan Sepeda")
st.pyplot(fig)
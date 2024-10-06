import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
st.title('Bike Sharing Dataset')
tab1, tab2= st.tabs(["Pertanyaan 1", "Pertanyaan 2"])
 
with tab1:
    # Mulai melakukan gathering pada data
    st.header("Gathering Data")

    # Membaca file data dengan format csv dan menampilkannya
    day_df = pd.read_csv("day.csv")
    st.dataframe(day_df.head())
    st.caption('Dengan menggunakan function read_csv() program akan membaca file csv yang kita lampirkan, lalu akan ditampilkan beberapa dengan function head()')

    #Mulai melakukan assessing data
    st.header("Assessing Data")

    #Menampilkan info dari data 'day'
    st.subheader('Info Data')
    st.dataframe(day_df.dtypes)
    #Menganalisis apakah ada missing value pada data tersebut
    st.subheader('Missing Value')
    null_values = day_df.isnull().sum()
    st.write(null_values)
    st.caption('Tidak terdapat missing value pada data')
    #Menganalisis apakah ada data yang terduplikat pada data tersebut
    st.subheader('Data Duplikat')
    st.write('Jumlah data duplikat : ' + str(day_df.duplicated().sum()))

    #Mulai melakukan cleaning pada data berdasarkan hasil analisis tadi
    st.header("Cleaning Data")
    #Mengubah tipe data pada kolom 'dteday' yang semula object menjadi datetime
    for column in datetime_columns:
     day_df[column]= pd.to_datetime(day_df[column])
    #Menampilkan info terkini dari data yang sudah melalui proses cleaning
    st.dataframe(day_df.dtypes)
    st.caption('Tipe data untuk kolom dteday yang semula object berhasil diganti dengan tipe data datetime')

    #Mulai melakukan tahap exploratory pada data
    st.header("## Exploratory Data Analysis (EDA)")
    #Menampilkan keseluruhan data
    st.subheader('Tabel Data')
    st.dataframe(day_df.describe(include="all"))
    #Menggabungkan kolom holiday dan kolom cnt pada data tersebut
    st.subheader('Tabel Gabungan Antara Kolom Holiday dan Count')
    join_day = day_df.groupby(by='holiday').agg({'cnt':['mean', 'max', 'min']})
    st.dataframe(join_day)
    text = st.text_area(
        "Insight",
        " Exploratory data menggunakan describe() dan agg() untuk mengelompokkan data"
        " berdasarkan hari libur dan jumlah penyewa sepeda yang nantinya menentukan"
        " pengaruh dari hari libur terhadap total dari penyewa sepeda."
    )

    #Mulai melakukan visualisasi dan explanatory analysis
    st.header("Visualization & Explanatory Analysis")
    #Menampilkan diagram untuk kolom holiday dan cnt
    st.bar_chart(day_df.groupby('holiday')['cnt'].mean())
    st.caption('Holiday(0 : Bukan Hari Libur Nasional, 1 : Hari Libur Nasional)')
    #Melakukan explanatory analysis
    text = st.text_area(
        "Insight",
        "Hasil visualisasi data pertama menunjukkan bahwa tingkat penyewaan sepeda pada hari"
        " libur nasional lebih rendah daripada hari biasa.")
    
    #Menjabarkan kesimpulan dari hasil analisis pada data 'day'
    st.header("Conclusion")
    text = st.text_area(
        "Jawaban Pertanyaan 1",
        "Pada hari libur nasioal, minat bersepeda penyewa menurun dibandingkan dengan hari"
        " biasa yang bukan hari libur nasional. Hal ini terjadi karena adanya kemungkinan"
        " dari penggunaan waktu penyewa. Hari libur biasa dimanfaatkan untuk berkumpul"
        " dengan keluarga ataupun teman. Dan ketika bepergian, mereka lebih memilih untuk"
        " menggunakan transportasi yang lebih nyaman salah satunya mobil atau bus. Hasil"
        " analisis ini bisa digunakan untuk mengubah target konsumen kepada para wisatawan"
        " yang sedang berkunjung ke kota tersebut, berikan penawaran tur wisata bersepeda"
        " untuk wisatawan agar menambah jumlah penyewa di hari libur.")

with tab2:
    #Mulai melakukan gathering pada data
    st.header("Gathering Data")

    #Membaca data 'hour' dengan format csv lalu menampilkannya
    hour_df = pd.read_csv("hour.csv")
    st.dataframe(hour_df.head())
    st.caption('Dengan menggunakan function read_csv() program akan membaca file csv yang kita lampirkan, lalu akan ditampilkan beberapa dengan function head()')

    #Mulai melakukan assessing pada data
    st.header("Assessing Data")

    #Menampilkan info dari data 'hour'
    st.subheader('Info Data')
    st.dataframe(day_df.dtypes)
    #Menganalisis apakah ada missing value pada data tersebut
    st.subheader('Missing Value')
    null_values = hour_df.isna().sum()
    st.write(null_values)
    st.caption('Tidak terdapat missing value pada data')
    #Menganalisis apakah ada data yang terduplikat pada data tersebut
    st.subheader('Data Duplikat')
    st.write('Jumlah data duplikat : ' + str(hour_df.duplicated().sum()))

    #Mulai melakukan cleaning pada data berdasarkan hasil analisis tadi
    st.header("Cleaning Data")
    #Mengubah tipe data pada kolom 'dteday' yang semula object menjadi datetime
    for column in datetime_columns:
     hour_df[column]= pd.to_datetime(hour_df[column])
    #Menampilkan info terkini dari data yang sudah melalui proses cleaning
    st.dataframe(hour_df.dtypes)
    st.caption('Tipe data untuk kolom dteday yang semula object berhasil diganti dengan tipe data datetime')

    #Mulai melakukan tahap exploratory pada data
    st.header("## Exploratory Data Analysis (EDA)")
    #Menampilkan keseluruhan data
    st.subheader('Tabel Data')
    st.dataframe(hour_df.describe(include="all"))
    #Menggabungkan kolom season dan kolom hr pada data tersebut
    st.subheader('Tabel Gabungan Antara Kolom Season dan Hours')
    join_hour = hour_df.groupby(by='season').agg({'hr':['mean', 'max', 'min']})
    st.dataframe(join_hour)
    text = st.text_area(
        "Insight",
        " Exploratory data menggunakan describe() dan agg() untuk mengelompokkan data"
        " berdasarkan season dan hours yang nantinya menentukan pengaruh dari musim tahunan"
        " terhadap durasi user bersepeda perjamnya."
    )

    #Mulai melakukan visualisasi dan explanatory analysis
    st.header("Visualization & Explanatory Analysis")
    #Menampilkan diagram untuk kolom holiday dan cnt
    avg=hour_df.groupby('season')['hr'].mean()
    seasons_label = {1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}
    plt.figure(figsize=(7,7))
    plt.pie(avg, labels=avg.index.map(seasons_label), autopct='%1.1f%%', startangle=90, colors=['#f7e0b8','#bbeed7','#b2e6e9','#f7cde1'])
    plt.axis('equal')
    st.pyplot(plt)
    st.title('Average Bike Rentals by Season')
    #Melakukan explanatory analysis
    text = st.text_area(
        "Insight",
        " Hasil visualisasi data kedua menunjukkan bahwa durasi user bersepeda tiap jamnya pada"
        " musim spring menurun daripada musim lainnya.")
    
    #Menjabarkan kesimpulan dari hasil analisis pada data 'hour'
    st.header("Conclusion")
    text = st.text_area(
        "Jawaban Pertanyaan 2",
        " Pada hari libur nasioal, minat bersepeda penyewa menurun dibandingkan dengan hari"
        " Dari hasil analisis kedua, didapatkan bahwa minat bersepeda penyewa pada musim"
        " spring lebih rendah dibandingkan musim lainnya. Hal ini bisa terjadi karena pada"
        " musim semi tidak banyak orang yang berminat untuk melakukan aktivitas di luar"
        " karena cuaca peralihan dari musim dingin ke musim panas ini terkadang tidak stabil."
        " Efek musim dingin juga belum sepenuhnya hilang, jalan yang licin membuat para"
        " penyewa mengurangi durasi bersepeda. Berdasarkan hasil analisis, pemilik rental"
        " bisa meningkatkan kualitas sepeda pada musim ini dan memberikan diskon khusus musim"
        " semi agar penyewa tidak ragu untuk bersepeda di musim semi.")

    




 

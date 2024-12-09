import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Set page configuration at the very beginning of the script
st.set_page_config(page_title="Pengelolaan Keuangan Pribadi", layout="wide")

# CSS for Background Animation and Theme
st.markdown(
    """
    <style>
    .main {
        background-color: #F0F2F6;
        transition: background-color 0.5s ease;
    }
    body[data-theme="dark"] .main {
        background-color: #181818;
    }
    .bg-animation {
        position: absolute;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%);
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%); }
        50% { background: radial-gradient(circle, rgba(148,187,233,1) 0%, rgba(238,174,202,1) 100%); }
        100% { background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML for Background Animation
components.html(
    """
    <div class="bg-animation"></div>
    """,
    height=0,
    width=0,
)

# Kelas untuk Pengelolaan Keuangan
class PengelolaanKeuangan:
    def __init__(self):
        self.saldo = 0.0
        self.transaksi = []

    def tambah_pemasukan(self, jumlah, keterangan):
        self.saldo += jumlah
        self.transaksi.append(('Pemasukan', jumlah, keterangan))

    def tambah_pengeluaran(self, jumlah, keterangan):
        self.saldo -= jumlah
        self.transaksi.append(('Pengeluaran', jumlah, keterangan))

    def lihat_saldo(self):
        return self.saldo

    def lihat_transaksi(self):
        return self.transaksi

# Inisialisasi kelas Pengelolaan Keuangan
keuangan = PengelolaanKeuangan()

# Judul aplikasi
st.title("Aplikasi Pengelolaan Keuangan Pribadi")

# Menu navigasi
with st.sidebar:
    pilihan = option_menu("Menu", ["Tambah Pemasukan", "Tambah Pengeluaran", "Lihat Saldo", "Lihat Transaksi", "Ganti Tema"],
                          icons=['plus', 'minus', 'wallet', 'list', 'gear'], menu_icon="cast", default_index=0)

# Tambah Pemasukan
if pilihan == "Tambah Pemasukan":
    st.subheader("Tambah Pemasukan")
    jumlah = st.number_input("Masukkan jumlah pemasukan: Rp", min_value=0.0)
    keterangan = st.text_input("Masukkan keterangan")
    if st.button("Tambah Pemasukan"):
        keuangan.tambah_pemasukan(jumlah, keterangan)
        st.success("Pemasukan berhasil ditambahkan!")

# Tambah Pengeluaran
elif pilihan == "Tambah Pengeluaran":
    st.subheader("Tambah Pengeluaran")
    jumlah = st.number_input("Masukkan jumlah pengeluaran: Rp", min_value=0.0)
    keterangan = st.text_input("Masukkan keterangan")
    if st.button("Tambah Pengeluaran"):
        keuangan.tambah_pengeluaran(jumlah, keterangan)
        st.success("Pengeluaran berhasil ditambahkan!")

# Lihat Saldo
elif pilihan == "Lihat Saldo":
    st.subheader("Lihat Saldo")
    saldo = keuangan.lihat_saldo()
    st.write(f"Saldo saat ini: Rp {saldo:.2f}")

# Lihat Transaksi
elif pilihan == "Lihat Transaksi":
    st.subheader("Lihat Transaksi")
    transaksi = keuangan.lihat_transaksi()
    if transaksi:
        for jenis, jumlah, keterangan in transaksi:
            st.write(f"{jenis}: Rp {jumlah:.2f} - {keterangan}")
    else:
        st.write("Belum ada transaksi")

# Ganti Tema
elif pilihan == "Ganti Tema":
    st.subheader("Ganti Tema")
    tema = st.selectbox("Pilih Tema", ["Default", "Dark Mode"])
    if tema == "Dark Mode":
        st.markdown(
            """
            <style>
            body {
                background-color: #181818;
                color: #FFFFFF;
            }
            .main {
                background-color: #181818;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            body {
                background-color: #F0F2F6;
                color: #000000;
            }
            .main {
                background-color: #F0F2F6;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Menjalankan aplikasi Streamlit
if __name__ == '__main__':
    st.set_page_config(page_title="Pengelolaan Keuangan Pribadi")

import matplotlib.pyplot as plt

# Data awal
barang = ["Barang A", "Barang B", "Barang C"]
stok_awal = [100, 200, 150]
pembelian = [50, 30, 20]
retur_pembelian = [5, 3, 2]
penjualan = [30, 50, 40]
retur_penjualan = [3, 5, 4]

# Hitung stok akhir
stok_akhir = [
    stok_awal[i] + pembelian[i] - retur_pembelian[i] - penjualan[i] + retur_penjualan[i]
    for i in range(len(barang))
]

# Buat subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Bar Chart
axs[0, 0].bar(barang, stok_awal, color='blue', label='Stok Awal')
axs[0, 0].bar(barang, stok_akhir, color='orange', label='Stok Akhir', alpha=0.7)
axs[0, 0].set_title('Perubahan Stok Barang')
axs[0, 0].set_ylabel('Jumlah Stok')
axs[0, 0].legend()

# Pie Chart Stok Awal
axs[0, 1].pie(stok_awal, labels=barang, autopct='%1.1f%%', startangle=140)
axs[0, 1].set_title('Distribusi Stok Awal')

# Histogram Pembelian dan Penjualan
axs[1, 0].hist([pembelian, penjualan], bins=5, label=['Pembelian', 'Penjualan'], color=['green', 'red'])
axs[1, 0].set_title('Histogram Pembelian dan Penjualan')
axs[1, 0].set_ylabel('Frekuensi')
axs[1, 0].legend()

# Line Chart
axs[1, 1].plot(barang, stok_awal, marker='o', label='Stok Awal')
axs[1, 1].plot(barang, stok_akhir, marker='o', label='Stok Akhir')
axs[1, 1].set_title('Stok Awal vs Stok Akhir')
axs[1, 1].set_ylabel('Jumlah Stok')
axs[1, 1].legend()

plt.tight_layout()
plt.show()

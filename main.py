import pandas as pd
import numpy as np

# Dosya yolunu tam olarak belirtiyoruz
file_path = 'excel_files/soru1_2_data.xlsx'

# Dosyayı yükle
df = pd.read_excel(file_path)

# Veriyi numpy array'e çevir
data = df.to_numpy()


# Contrast Stretching fonksiyonu
def contrast_stretching(data, L=256):
    min_val = np.min(data)
    max_val = np.max(data)
    rows, cols = data.shape
    stretched_data = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            stretched_data[i, j] = ((data[i, j] - min_val) / (max_val - min_val)) * (L - 1)

    return stretched_data


# Contrast Stretching uygulaması
stretched_data = contrast_stretching(data)

# Sonuçları daha okunaklı bir formatta yazdırma
with np.printoptions(precision=2, suppress=True):
    print("Contrast Stretching Sonucu:\n", stretched_data)

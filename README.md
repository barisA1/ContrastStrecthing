# 📊 Contrast Stretching Script

Bu Python scripti, bir Excel dosyasından veri okuyup contrast stretching işlemi uygulamak için kullanılabilir.

## 📄 İçindekiler
- [Gereksinimler](#-gereksinimler)
- [Kullanım](-#kullanım)
- [Fonksiyonlar](#-fonksiyonlar)
- [Örnek](#-örnek)
- [İletişim](#-iletişim)

## 🛠️ Gereksinimler

Bu scriptin çalışabilmesi için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

- `pandas`
- `numpy`
- `openpyxl` (pandas'ın Excel dosyalarını okuyabilmesi için)

Bu kütüphaneleri aşağıdaki komutla yükleyebilirsiniz:

```sh
pip install pandas numpy openpyxl
```

## 🎯 Kullanım

### 1. Dosya Yolu Ayarlaması
`main.py` dosyasında, verilerin okunacağı Excel dosyasının yolunu belirtin. Örneğin:

```python
file_path = r'C:\\Users\\Barış\\Desktop\\soru1_2_data.xlsx'
```

### 2. Scripti Çalıştırma
Aşağıdaki komutla scripti çalıştırın:

```sh
python main.py
```

### 3. Sonuçların Görüntülenmesi
Script çalıştırıldıktan sonra, contrast stretching işlemi uygulanmış veriler terminalde görüntülenecektir.

## 📑 Fonksiyonlar

### `contrast_stretching(data, L=256)`

Bu fonksiyon, verilen veri üzerinde contrast stretching işlemi uygular. 

- `data`: Numpy array formatında veri.
- `L`: Çıkış verisinin maksimum değeri (varsayılan 256).

Fonksiyon, işlem uygulanmış veriyi numpy array formatında döner.

## 📝 Örnek

Örnek bir Excel dosyasının nasıl yükleneceği ve işleneceği aşağıda gösterilmiştir:

```python
import pandas as pd
import numpy as np

file_path = r'C:\\Users\\Barış\\Desktop\\soru1_2_data.xlsx'
df = pd.read_excel(file_path)
data = df.to_numpy()

stretched_data = contrast_stretching(data)

with np.printoptions(precision=2, suppress=True):
    print("Contrast Stretching Sonucu:\n", stretched_data)
```

## ℹ️ Ek Bilgiler
Bu script, özellikle görüntü işleme ve veri analizi projelerinde kullanılmak üzere tasarlanmıştır. Excel dosyanızdaki verileri contrast stretching ile dönüştürerek daha iyi analiz edilebilir hale getirebilirsiniz.

## 🤝 Katılım
Projeye katkıda bulunmak isterseniz:

- Bu depoyu çatallayın (fork) ve geliştirmelerinizi yapın.
- Yeni özellikler eklemek veya hataları düzeltmek için Pull Talepler (Pull Requests) gönderin.
- Hataları bildirmek veya önerilerde bulunmak için konu (issue) açın.

## 📬 İletişim

Herhangi bir soru veya öneriniz için lütfen [aktasb723@gmail.com] e posta adresi ile iletişime geçin.


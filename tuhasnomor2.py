import cv2
import numpy as np

# Membuat citra hitam putih 100x100
image = np.zeros((100, 100), dtype=np.uint8)

# Menentukan bagian atas citra menjadi putih (nilai maksimum)
image[:50, :] = 255  # Bagian atas citra putih (0-50 baris), sisanya hitam

# Menyimpan citra yang dihasilkan
cv2.imwrite('citra_hitam_putih.jpg', image)

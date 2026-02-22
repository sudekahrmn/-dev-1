import numpy as np
import matplotlib.pyplot as plt

# =========================
# TEMEL FREKANS (3 kişi)
# =========================
f0 = 13 + 31 + 9   # 53 Hz

f1 = f0
f2 = f0 / 2
f3 = 10 * f0

# =========================
# Örnekleme Frekansı
# =========================
fs = 5000  # Nyquist'ten büyük güvenli değer

# =========================
# Zaman Ekseni (3 periyot)
# =========================
T = 1 / f2   # en büyük periyot f2 olduğu için
t = np.arange(0, 3*T, 1/fs)

# =========================
# Sinyaller
# =========================
x1 = np.sin(2*np.pi*f1*t)
x2 = np.sin(2*np.pi*f2*t)
x3 = np.sin(2*np.pi*f3*t)

# =========================
# Grafikler
# =========================
plt.figure(figsize=(10,7))

plt.subplot(3,1,1)
plt.plot(t, x1)
plt.title("f1 = 53 Hz")

plt.subplot(3,1,2)
plt.plot(t, x2)
plt.title("f2 = 26.5 Hz")

plt.subplot(3,1,3)
plt.plot(t, x3)
plt.title("f3 = 530 Hz")

plt.tight_layout()
plt.show()

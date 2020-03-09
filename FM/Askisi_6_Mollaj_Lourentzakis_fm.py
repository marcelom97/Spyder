# %%
from fft_modules import amfi_fasma, mono_fasma
from numpy import pi, cos, linspace, sin
import matplotlib.pyplot as plt

# πληροφορία
Am = 1
fm = 2000
Tm = 1 / fm

# Φέρον
Ac = 3
fc = 20000
Tc = 1 / fc

number_of_signal_periods = 3
Tmax = Tm * number_of_signal_periods
B = max(fc, fm)
Nyquist = 2 * B
Fs = 100 * Nyquist
Ts = 1 / Fs

kf = 2 * pi * 4000
m = (kf * Am) / (2 * pi * fm)
print("Fs:", Fs, "Ts:", Ts)

t = linspace(0, Tmax, int(Tmax / Ts))
data = Am * cos(2 * pi * fm * t)
carrier = Ac * cos(2 * pi * fc * t)
FM = Ac * cos((2 * pi * fc * t) + m * sin(2 * pi * fm * t))

plt.figure(1)
plt.plot(t, carrier)
plt.plot(t, data)
plt.title("Σήμα πληροφορίας και φέρον")
plt.ylabel("Πλάτος(V)")
plt.xlabel("Χρόνος(sec)")
plt.tight_layout()

plt.figure(2)
plt.plot(t, FM)
plt.plot(t, data)
plt.title("Σήμα πληροφορίας και FM")
plt.ylabel("Πλάτος(V)")
plt.xlabel("Χρόνος(sec)")
plt.tight_layout()

plt.figure(3)
plt.subplot(2, 1, 1)
amfi_frequincies, amfipleuro = amfi_fasma(FM, t)
plt.plot(amfi_frequincies, amfipleuro)
#plt.stem(amfi_frequincies, amfipleuro)
plt.xlim(-fc - ((m + 4)*fm), fc + ((m + 4)*fm))
plt.title("Αμφίπλευρο φάσμα FM σήματος")
plt.ylabel("Πλάτος(V)")
plt.xlabel("Συχνότητα(Hz)")
plt.tight_layout()

plt.subplot(2, 1, 2)
mono_frequincies, monopleuro = mono_fasma(FM, t)
plt.plot(mono_frequincies, monopleuro)
#plt.stem(mono_frequincies, monopleuro)
plt.xlim(fc - ((m + 4)*fm), fc + ((m + 4)*fm))
plt.title("Μονόπλευρο φάσμα FM σήματος")
plt.ylabel("Πλάτος(V)")
plt.xlabel("Συχνότητα(Hz)")
plt.tight_layout()

print("Πλάτος του διαμορφωμένου σήματος:", max(FM))
print("Μέση κανονικοποιημένη ισχύς φέροντος:", (Ac ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς πληροφοριακού σήματος:", (Am ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς FM σήματος:", (max(FM) ** 2) / 2)
print("Απόκλιση συχνότητας:", m * fm)
print("Δείκτης διαμόρφωσης:", m)
print("Εύρος ζώνης πληροφοριακού σήματος:", fm)
print("Εύρος ζώνης FM σήματος:", 2 * (m + 1) * fm)

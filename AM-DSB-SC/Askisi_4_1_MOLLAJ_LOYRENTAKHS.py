# %%
from numpy import pi, cos, linspace
import matplotlib.pyplot as plt
from fft_modules import amfi_fasma, mono_fasma

# data
Am = float(input("Δώσε πλάτος σήματος πληροφορίας:"))
fm = float(input("Δώσε συχνότητα σήματος πληροφορίας:"))
Tm = 1 / fm

# carrier
Ac = float(input("Δώσε πλάτος φέρον σήματος:"))
fc = float(input("Δώσε συχνότητα φέρον σήματος:"))
Tc = 1 / fc

signal_periods = 3  # Πόσες Περιόδους θέλω να εμφανίσω
Tmax = signal_periods * Tm  # Αριθμός επί περίοδος
B = max(fc, fm)  # Eύρος ζώνης
Nyquist = 2 * B  # Συχνότητα Nyquist

Fs = 10 * Nyquist  # Συχνότητα δειγματοληψία 10 φορές του Nyquist
Ts = 1 / Fs  # Περίοδος δειγματοληψίας

print("Fs:", Fs)
print("Ts:", Ts)

t = linspace(0, Tmax, int(Tmax/Ts))  # Πίνακας χρόνου

data = Am * cos(2 * pi * fm * t)  # Σήμα Πληροφορίας
carrier = Ac * cos(2 * pi * fc * t)  # Φέρος Σήμα
AM_DSB_SC = data * carrier  # Διαμορφομένο Σήμα

USB = data * Ac  # Άνω πλευρική
LSB = -Ac * data  # Κάτω πλευρική

plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(t, data)
plt.title("Πληροφορία")


plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Φέρον")

plt.subplot(3, 1, 3)
plt.plot(t, AM_DSB_SC)
plt.plot(t, USB)
plt.plot(t, LSB)
plt.title("AM-DSB-SC with USB & LSB")

plt.figure(2)
frequencies, amfipleuro = amfi_fasma(AM_DSB_SC, t)  # Αμφίπλευρο φάσμα διαμορφωμένου σήματος
plt.subplot(2, 1, 1)
plt.stem(frequencies, amfipleuro)
plt.title("Αμφίπλευρο Φάσμα")
plt.ylim(0, 1.5*Ac)
plt.xlim(-fc-5*fm, fc+5*fm)
plt.grid(axis='both')

frequencies, monopleuro = mono_fasma(AM_DSB_SC, t)  # Μονόπλευρο φάσμα διαμορφωμένου σήματος
plt.subplot(2, 1, 2)
plt.stem(frequencies, monopleuro)
plt.title("Μονόπλευρο Φάσμα")
plt.ylim(0, 1.5*Ac)
plt.xlim(-fc-5*fm, fc+5*fm)
plt.grid(axis='both')

print("Μέγιστη τιμή πλάτους του διαμορφωμένου σήματος:", max(AM_DSB_SC))
print("Ελάχιστη τιμή πλάτους του διαμορφωμένου σήματος:", min(AM_DSB_SC))
print("Μέση κανονικοποιημένη ισχύς φέροντος:", (Ac ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς πληροφοριακού σήματος:", (Am ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς ΑΜ DSB-SC σήματος:", (((Ac*Am) / 2) ** 2) / 2 + (((Ac*Am) / 2) ** 2) / 2)
print("Απόδοση ισχύος: 100%")
print("Εύρος ζώνης πληροφοριακού σήματος:", fm, "Hz")
print("Εύρος ζώνης ΑΜ DSB-SC σήματος από:", fc - fm, " έως:", fc + fm, "Hz")

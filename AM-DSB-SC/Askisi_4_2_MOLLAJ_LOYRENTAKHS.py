# %%
from numpy import pi, cos, linspace
import matplotlib.pyplot as plt
from fft_modules import amfi_fasma, mono_fasma

# data signal No one
Am1 = float(input("Δώσε πλάτος σήματος πληροφορίας_1:"))
fm1 = float(input("Δώσε συχνότητα σήματος πληροφορίας_1:"))
Tm1 = 1 / fm1

# data signal No two
Am2 = float(input("Δώσε πλάτος σήματος πληροφορίας_2:"))
fm2 = float(input("Δώσε συχνότητα σήματος πληροφορίας_2:"))
Tm2 = 1 / fm2

# carrier
Ac = float(input("Δώσε πλάτος φέρον σήματος:"))
fc = float(input("Δώσε συχνότητα φέρον σήματος:"))
Tc = 1 / fc

B = max(fc, fm1, fm2)  # Eύρος ζώνης
Nyquist = 2 * B  # Συχνότητα Nyquist
number_of_signal_periods = 3  # Πόσες Περιόδους θέλω να εμφανίσω
Tmax = max(Tm1, Tm2, Tc) * number_of_signal_periods  # Αριθμός επί περίοδος
Fs = 10 * Nyquist  # Συχνότητα δειγματοληψία 10 φορές του Nyquist
Ts = 1 / Fs  # Περίοδος δειγματοληψίας

print("Fs:", Fs)
print("Ts:", Ts)

t = linspace(0, Tmax, int(Tmax / Ts))  # Πίνακας χρόνου

signal_1 = Am1 * cos(2 * pi * fm1 * t)  # Σήμα Πληροφορίας_1
signal_2 = Am2 * cos(2 * pi * fm2 * t)  # Σήμα Πληροφορίας_2
data = signal_1 + signal_2  # Πληροφορία_1 + Πληροφορία_2
carrier = Ac * cos(2 * pi * fc * t)  # Φέρος Σήμα
AM_DSB_SC = carrier * data  # Διαμορφομένο Σήμα
USB = Ac * data  # Άνω πλευρική
LSB = -Ac * data  # Κάτω πλευρική

plt.figure(1)
plt.subplot(4, 1, 1)
plt.plot(t, signal_1)
plt.title("Πληροφορία_1")

plt.subplot(4, 1, 2)
plt.plot(t, signal_2)
plt.title("Πληροφορία_2")

plt.subplot(4, 1, 3)
plt.plot(t, carrier)
plt.title("Φέρον")

plt.subplot(4, 1, 4)
plt.plot(t, AM_DSB_SC)
plt.plot(t, USB)
plt.plot(t, LSB)
plt.title("AM-DSB-SC")

plt.figure(2)

frequencies, amfipleuro = amfi_fasma(AM_DSB_SC, t)  # Αμφίπλευρο φάσμα διαμορφωμένου σήματος
plt.subplot(2, 1, 1)
plt.stem(frequencies, amfipleuro)
plt.ylim(0, 1.5*Ac)
plt.xlim(-fc-5*max(fm1, fm2), fc+5*max(fm1, fm2))
plt.grid(axis='both')

frequencies, monopleuro = mono_fasma(AM_DSB_SC, t)  # Μονόπλευρο φάσμα διαμορφωμένου σήματος
plt.subplot(2, 1, 2)
plt.stem(frequencies, monopleuro)
plt.ylim(0, 3*Ac)
plt.xlim(-fc-5*max(fm1, fm2), fc+5*max(fm1, fm2))
plt.grid(axis='both')

print("Μέγιστη τιμή πλάτους του διαμορφωμένου σήματος:", max(USB))
print("Ελάχιστη τιμή πλάτους του διαμορφωμένου σήματος:", min(LSB))
print("Μέση κανονικοποιημένη ισχύς φέροντος:", (Ac ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς του σήματος Πληροφορία_1:", (Am1 ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς του σήματος Πληροφορία_2:", (Am2 ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς Πληροφορίας:", (max(data) ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς ΑΜ DSB-SC σήματος:", ((((Ac * Am1) / 2) ** 2) / 2) + ((((Ac * Am1) / 2) ** 2) / 2) + ((((Ac * Am2) / 2) ** 2) / 2) + ((((Ac * Am2) / 2) ** 2) / 2))
print("Απόδοση ισχύος: 100%")
print("Εύρος ζώνης πληροφοριακού σήματος:", max(fm1, fm2), "Hz")
print("Εύρος ζώνης ΑΜ DSB-SC σήματος από:", fc - max(fm1, fm2), "έως:", fc + max(fm1, fm2))

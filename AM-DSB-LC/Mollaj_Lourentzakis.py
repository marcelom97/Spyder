# %%
from fft_modules import mono_fasma
from numpy import cos, pi, linspace, arange
import matplotlib.pyplot as plt

# Data
Ad = float(input("Δώσε πλάτος πληροφορίας:")) # Πλάτος
fd = float(input("Δώσε συχνότητα πληροφορίας:"))  # Συχνότητα
Td = 1 / fd  # Περίοδος

# Carrier
Ac = float(input("Δώσε πλάτος φέροντος:")) # Πλάτος
fc = float(input("Δώσε συχνότητα φέροντος:"))  # Συχνότητα
Tc = 1 / fc  # Περίοδος

m = Ad / Ac  # Δείκτης διαμόρφωσης

number_of_signal_periods = 3  # αριθμός περιόδων του σήματος
Tmax = number_of_signal_periods * Td  # Συνολική χρονική διάρκεια του σήματος
samples_per_period = 100  # αριθμός δειγμάτων ανά περίοδο
Ts = Tc / samples_per_period  # Χρόνος δειγματοληψίας
Fs = 1 / Ts  # συχνότητα δειγματοληψίας

print("Fs:", Fs)
print("Ts: ", Ts)

t = linspace(0, Tmax, int(Tmax / Ts))  # πίνακας χρόνου

data = Ad * cos(2 * pi * fd * t)  # Σήμα πληροφορίας
carrier = Ac * cos(2 * pi * fc * t)  # Σήμα που θα κουβαλίσει την πληροφορία
AM_DSB_LC = Ac * (1 + (m * cos(2 * pi * fd * t))) * cos(2 * pi * fc * t)  # Διαμορφομένο σήμα
FULL_AM_USB = data + Ac  # Άνω περιβάλλουσα
FULL_AM_LSB = -1 * data - Ac  # Κάτω περιβάλλουσα

plt.figure(1)
plt.subplot(4, 1, 1)
plt.plot(t, data)
plt.title("Πληροφορία")
plt.yticks(arange(-Ad, Ad + 1, step=Ad))

plt.subplot(4, 1, 2)
plt.plot(t, carrier)
plt.title("Φέρον Σημα")
plt.yticks(arange(-Ac, Ac + 1, step=Ac))

plt.subplot(4, 1, 3)
plt.plot(t, AM_DSB_LC)
plt.title("Διαμορφομένο σήμα")

plt.subplot(4, 1, 4)
plt.plot(t, AM_DSB_LC)
plt.plot(t, FULL_AM_USB)
plt.plot(t, FULL_AM_LSB)
plt.title("Διαμορφομένο σήμα με Άνω και Κάτω πλευρική")
plt.subplots_adjust(hspace=0.35)

Amax = max(FULL_AM_USB)
Amin = min(FULL_AM_USB)

print("Amax:", Amax)
print("Amin:", Amin)
print("m:", m)
print("Μέση κανονικοποιημένη ισχύς φέροντος: ",(Ac**2)/2)
print("Μέση κανονικοποιημένη ισχύς πληροφορίας: ", (Ad**2)/2)
print("Αέση κανονικοποιημένη ισχύς ΑΜ DSB-LC σήματος: ", (Ac**2)/2+(((Ad/2)**2)/2)+(((Ad/2)**2)/2))
print("Απόδοση ισχύος: ", str(((m**2)/(2+(m**2)) * 100)) + "%")

frequencies, mono = mono_fasma(AM_DSB_LC, t)

plt.figure(2)
# plt.plot(frequencies, mono)
plt.stem(frequencies, mono)
plt.xlim(fc - 5 * fd, fc + 5 * fd)
plt.ylim(0, 3 * Ac)
plt.axhline(y=Ac, ls=':')
plt.axhline(y=Ad / 2, ls=':')

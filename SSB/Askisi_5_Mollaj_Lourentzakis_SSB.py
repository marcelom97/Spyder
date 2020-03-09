# %%
from fft_modules import mono_fasma, amfi_fasma
from numpy import pi, cos, linspace
import matplotlib.pyplot as plt

# data
Am = 1
fm = 1000
Tm = 1 / fm

# carrier
Ac = 3
fc = 10000
Tc = 1 / fc

B = max(fc, fm)
Nyquist = 2 * B
number_of_signal_periods = 3
Tmax = max(Tc, Tm) * number_of_signal_periods

Fs = 10 * Nyquist
Ts = 1 / Fs

t = linspace(0, Tmax, Tmax / Ts)

# Σχήμα που δειχνει την πληροφορία μαζι με το αμφίπλευρο και το μον΄΄οπλευρο φασμα της
data = Am * cos(2 * pi * fm * t)
carrier = Ac * cos(2 * pi * fc * t)

plt.figure(1)
amfi_freq, amfipleuro = amfi_fasma(data, t)
mono_freq, monopleuro = mono_fasma(data, t)

plt.subplot(3, 1, 1)
plt.plot(t, data)
plt.title("Πληροφορία")

plt.subplot(3, 1, 2)
plt.stem(amfi_freq, amfipleuro)
plt.xlim(-2 * fm, 2 * fm)
plt.ylim(0, Am)
plt.title("Αμφίπλευρο φάσμα πληροφοριακού σήματος")

plt.subplot(3, 1, 3)
plt.stem(mono_freq, monopleuro)
plt.xlim(0, 2 * fm)
plt.ylim(0, 1.5 * Am)
plt.title("Μονόπλευρο φάσμα πληροφοριακού σήματος")


# Σχήμα που δείχνει το Φέρον μαζί με το αμφίπλευρο και το μονόπλευρο φάσμα του
plt.figure(2)
amfi_freq, amfipleuro = amfi_fasma(carrier, t)
mono_freq, monopleuro = mono_fasma(carrier, t)

plt.subplot(3, 1, 1)
plt.plot(t, carrier)
plt.title("Φέρον")

plt.subplot(3, 1, 2)
plt.stem(amfi_freq, amfipleuro)
plt.xlim(-2 * fc, 2 * fc)
plt.ylim(0, Ac)
plt.title("Αμφίπλευρο φάσμα φέροντος σήματος")

plt.subplot(3, 1, 3)
plt.stem(mono_freq, monopleuro)
plt.xlim(0, 2 * fc)
plt.ylim(0, 1.5 * Ac)
plt.title("Μονόπλευρο φάσμα φέροντος σήματος")

# Σχήμα που δείχνει το Σήμα μου στο σημείο 1
simio_1 = carrier * data
plt.figure(3)
amfi_freq, amfipleuro = amfi_fasma(simio_1, t)
mono_freq, monopleuro = mono_fasma(simio_1, t)

plt.subplot(3, 1, 1)
plt.plot(t, simio_1)
plt.title("Σήμα στο σημείο 1")

plt.subplot(3, 1, 2)
plt.stem(amfi_freq, amfipleuro)
plt.xlim(-1.5 * fc, 1.5 * fc)
plt.ylim(0, 1.5 * ((Ac*Am)/4))
plt.title("Αμφίπλευρο φάσμα σήματος στο σημείο 1")

plt.subplot(3, 1, 3)
plt.stem(mono_freq, monopleuro)
plt.xlim(0, 2 * fc)
plt.ylim(0, 1.5 * ((Ac*Am)/2))
plt.title("Μονόλευρο φάσμα σήματος στο σημείο 1")

# Σχήμα που δείχνει το Σήμα μου στο σημείο 2
shifted_data = Am * cos(2 * pi * fm * t + pi / 2)
shifted_carrier = Ac * cos(2 * pi * fc * t + pi / 2)
simio_2 = shifted_carrier * shifted_data
amfi_freq, amfipleuro = amfi_fasma(simio_2, t)
mono_freq, monopleuro = mono_fasma(simio_2, t)
plt.figure(4)
plt.subplot(3, 1, 1)
plt.plot(t, simio_2)
plt.title("Σήμα στο σημείο 2")

plt.subplot(3, 1, 2)
plt.stem(amfi_freq, amfipleuro)
plt.xlim(-1.5 * fc, 1.5 * fc)
plt.ylim(0, 1.5 * ((Ac*Am)/4))
plt.title("Αμφίπλευρο φάσμα σήματος στο σημείο 2")

plt.subplot(3, 1, 3)
plt.stem(mono_freq, monopleuro)
plt.xlim(0, 2 * fc)
plt.ylim(0, 1.5 * ((Ac*Am)/2))
plt.title("Μονόπλευρο φάσμα σήματος στο σημείο 2")

# Σχήμα που μου δείχνει το Σ΄ήμα μου στο σημείο 3 με πρόσημο +
simio_3_pos = simio_1 + simio_2
amfi_freq, amfipleuro = amfi_fasma(simio_3_pos, t)
mono_freq, monopleuro = mono_fasma(simio_3_pos, t)

plt.figure(5)
plt.subplot(3, 1, 1)
plt.plot(t, simio_3_pos)
plt.title("Σήμα στην έξοδο με + στο Α1 και + στο Α2")

plt.subplot(3, 1, 2)
plt.stem(amfi_freq, amfipleuro)
plt.xlim(-1.5 * fc, 1.5 * fc)
plt.ylim(0, Ac)
plt.title("Αμφίπλευρο φάσμα σήματος με + στο Α1 και + στο Α2")

plt.subplot(3, 1, 3)
plt.stem(mono_freq, monopleuro)
plt.xlim(0, 1.5 * fc)
plt.ylim(0, 1.5 * Ac)
plt.title("Μονόπλευρο φάσμα σήματος με + στο Α1 και + στο Α2")

# Σχήμα που μου δείχνει το Σ΄ήμα μου στο σημείο 3 με πρόσημο -
simio_3_neg = -simio_1 + simio_2
amfi_freq, amfipleuro = amfi_fasma(simio_3_neg, t)
mono_freq, monopleuro = mono_fasma(simio_3_neg, t)

plt.figure(6)
plt.subplot(3, 1, 1)
plt.plot(t, simio_3_neg)
plt.title("Σήμα στην έξοδο με - στο Α1 και + στο Α2")

plt.subplot(3, 1, 2)
plt.stem(amfi_freq, amfipleuro)
plt.xlim(-1.5 * fc, 1.5 * fc)
plt.ylim(0, Ac)
plt.title("Αμφίπλευρο φάσμα σήματος με - στο Α1 και + στο Α2")

plt.subplot(3, 1, 3)
plt.stem(mono_freq, monopleuro)
plt.xlim(0, 1.5 * fc)
plt.ylim(0, 1.5 * Ac)
plt.title("Μονόπλευρο φάσμα σήματος με - στο Α1 και + στο Α2")

print("Μέγιστη τιμή πλάτους του διαμορφωμένου σήματος στην περίπτωση 5:", max(simio_3_pos))
print("Μέγιστη τιμή πλάτους του διαμορφωμένου σήματος στην περίπτωση 6:", round(max(simio_3_neg), 2))
print("Μέση κανονικοποιημένη ισχύς φέροντος:", (Ac ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς πληροφοριακού σήματος:", (Am ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς διαμορφωμένου  σήματος στην περίπτωση 5:", (max(simio_3_pos) ** 2) / 2)
print("Μέση κανονικοποιημένη ισχύς διαμορφωμένου  σήματος στην περίπτωση 6:", round((max(simio_3_neg) ** 2) / 2, 2))
print("Εύρος ζώνης πληροφοριακού σήματος:", fm)
print("Εύρος ζώνης διαμορφωμένου σήματος στην περίπτωση 5:", abs(fc - (fc + fm)))
print("Εύρος ζώνης διαμορφωμένου σήματος στην περίπτωση 6:", abs(fc - (fc - fm)))

print("Ts: ",Ts, "Fs: ", Fs)
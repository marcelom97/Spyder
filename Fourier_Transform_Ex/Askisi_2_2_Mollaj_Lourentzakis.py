#%%
from numpy import pi, sin, cos, linspace, abs, arange, ndarray
import matplotlib.pyplot as plt
from fft_modules import amfi_fasma, mono_fasma, monopleyro_fasma
# amfipleyro_fasma υπολογίζει το μη κεντραρισμενο αμφιπλευρο φασμα πλάτους
# monopleyro_fasma υπολογίζει το μη κεντραρισμενο μονοπλευρο φασμα πλάτους
# amfi_fasma υπολογίζει το κεντραρισμενο αμφιπλευρο φασμα πλάτους
# mono_fasma υπολογίζει το κεντραρισμενο μονοπλευρο φασμα πλάτους

A1, A2, A3 = 2, 4, 8                                        # Πλάτοι
f1, f2, f3 = 100, 500, 1000                                 # συχνότητες
T1, T2, T3 = 1 / f1, 1 / f2, 1 / f3                         # Περίοδοι
B = max(f1, f2, f3)                                         # Εύρος συχνοτήτων
Nyquist_Freq = 2 * B
number_of_signal_periods = 3                                # Αριθμός περιόδων που θέλω να εμφανίσω
Tmax = number_of_signal_periods * T1                        # Αριθμός περιόδων επί την περίδο που θέλω
samples_per_period = 200 #1000                              # Αριθμός δειγμάτων ανα περίοδο
Ts = max(T1, T2, T3) / samples_per_period                   # Περίοδος Δειγματοληψίας
Fs = 1 / Ts
t = linspace (0, Tmax, int(Tmax / Ts))                      # Πίνακας χρόνου
total_samples = len(t)                                      # Αριθμός συνολικών δειγμάτων

print("Fs="+str(int(Fs)) + " Ts=" + str(Ts) + " total_samples=" + str(total_samples))

signal_1 = A1 * cos(2 * pi * f1 * t)
signal_2 = A2 * cos(2 * pi * f2 * t)
signal_3 = A3 * sin(2 * pi * f3 * t)

final_signal = signal_1 + signal_2 + signal_3

plt.figure(1)

plt.subplot(4,1,1)
plt.plot(t, signal_1)
plt.title("Signal 1")
plt.yticks(arange(-A1, A1 + 1, step=1))
    
plt.subplot(4,1,2)
plt.plot(t, signal_2)
plt.title("Signal 2")
plt.yticks(arange(-A2, A2 + 1, step=2))

plt.subplot(4,1,3)
plt.plot(t, signal_3)
plt.title("Signal 3")
plt.yticks(arange(-A3, A3 + 1, step=4))

plt.subplot(4,1,4)
plt.plot(t, final_signal)
plt.title("Sum of signals")
plt.yticks(arange(min(final_signal), max(final_signal) + 1, step=max(final_signal)/2))

plt.figure(2)

amfi_frequencies, amfipleyro = amfi_fasma(final_signal, t)  # Υπολογιστμός κεντραρισμένου Αμφίπλευρου φάσμα πλάτους
plt.plot(amfi_frequencies, amfipleyro)
plt.xlim(-2 * max(f1, f2, f3), 2 * max(f1, f2, f3))
plt.ylim(0, 10)
plt.title("Αμφίπλευρο φάσμα πλάτους")
plt.xlabel("<- Συχνότητα ->")
plt.ylabel("Πλάτος ->")

plt.figure(3)

mono_frequencies, monopleyro = mono_fasma(final_signal, t)  # Υπολογιστμός κεντραρισμένου Mονόπλευρου φάσμα πλάτους
plt.plot(mono_frequencies, monopleyro)
plt.xlim(-2 * max(f1, f2, f3), 2 * max(f1, f2, f3))
plt.ylim(0, 10)
plt.title("Μονόπλευρο φάσμα πλάτους")
plt.xlabel("<- Συχνότητα ->")
plt.ylabel("Πλάτος ->")

plt.figure(4)

esd = abs(monopleyro) ** 2              # Μέτρο μετασχηματισμού fourier στο τετράγωνο ειναι η ενεργειακή φασματική πυκνότητα
"""
Υπολογισμός Ενεργειακή φασματική πυκνότητα με For loop,
δεν μου βγάζει ακριβώς τις τιμές γιατί έχω και μερικά σημεία
πολύ κοντά στο 0 και τα προσθέτει στο τελικό
"""
cnt = float(0)
for n in range(0,len(esd)):
    cnt += float(esd[n])
print("Πυκνότητα:"+str(cnt))
"""
Υπολογισμός Ενεργειακή φασματική πυκνότητα με μπακαλίστικο τρόπο
αλλά πιστεύω το αποτέλεσμα να είναι πιο σωστό.
Πρώτα βρίσκω το μονόπλευρο φάσμα για κάθε σήμα,
μετά βρίσκω την ενεργειακή φασματική πυκνότητα για κάθε σήμα 
και τέλος έχω την τελική φασματική πυκνότητα που τα αθροίζω όλα
"""
#mono1_frequencies, monopleyro1 = mono_fasma(signal_1, t)
#mono2_frequencies, monopleyro2 = mono_fasma(signal_2, t)
#mono3_frequencies, monopleyro3 = mono_fasma(signal_3, t)
#esd1 = abs(monopleyro1) ** 2
#esd2 = abs(monopleyro2) ** 2
#esd3 = abs(monopleyro3) ** 2
#final_esd = max(esd1) + max(esd2) + max(esd3)
#print("Πυκνότητα:"+str(final_esd))

plt.plot(mono_frequencies, esd)             
plt.xlim(-2 * max(f1, f2, f3), 2 * max(f1, f2, f3))                              
plt.ylim(0, 2 * max(A1,A2,A3) ** 2 + 6)
plt.ylabel("Πλάτος ->")
plt.xlabel("<- Συχνότητα ->")
plt.title("Ενεργειακή φασματική πυκνότητα")
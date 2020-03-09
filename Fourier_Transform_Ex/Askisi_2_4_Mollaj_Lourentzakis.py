#%%
from numpy import pi, linspace, arange
from scipy import signal
import matplotlib.pyplot as plt
from fft_modules import amfipleyro_fasma, monopleyro_fasma, amfi_fasma, mono_fasma
#amfipleyro_fasma υπολογίζει το μη κεντραρισμενο αμφιπλευρο φασμα πλάτους
#monopleyro_fasma υπολογίζει το μη κεντραρισμενο μονοπλευρο φασμα πλάτους
#amfi_fasma υπολογίζει το κεντραρισμενο αμφιπλευρο φασμα πλάτους
#mono_fasma υπολογίζει το κεντραρισμενο μονοπλευρο φασμα πλάτους

A = 1
T = 0.02 * 5                                                    # Περίοδος
f = 1 / T                                                       # Συχνότητα

number_of_signal_periods = 5                                    # Αριθμός περιόδων που θέλω να εμφανίσω
Tmax = number_of_signal_periods * T                             # Αριθμός περιόδων επί την περίδο που θέλω
samples_per_period = 200                                        # Αριθμός δειγμάτων ανα περίοδο
Ts = T / samples_per_period                                     # Περίοδος Δειγματοληψίας
Fs = 1 / Ts
#print("A:"+str(A))
#print("T:"+str(T))
#print("f:"+str(f))
#print("Ts:"+str(Ts))
#print("Fs:"+str(Fs))
t = linspace (-2.5 * T, 2.5 * T, Tmax / Ts)                     # Πίνακας χρόνου
our_signal = A * signal.square(2 * pi * f * (t+T/4))            # Τετραγωνικός Παλμός
our_signal[t<-T/4] = 0                                          #Αφαιρώ
our_signal[t>T/4] = 0

plt.figure(1)
plt.plot(t, our_signal)
plt.xticks(arange(-0.05, 0.06, step=0.01))
plt.ylim(-2, 2)
plt.xlim(-0.05, 0.05)
plt.grid(axis="both") 
plt.title("Τετραγωνικός παλμός")
plt.ylabel("<- Πλάτος ->")
plt.xlabel("<- Χρόνος ->")

plt.figure(2)

plt.subplot(2, 1, 1)
amfi_frequencies, amfipleyro = amfi_fasma(our_signal,t)   # Υπολογιστμός κεντραρισμένου Αμφίπλευρου φάσμα πλάτους
plt.plot(amfi_frequencies, amfipleyro)
plt.ylim(0, 0.2)
plt.xlim(-Fs / 20, Fs / 20)
plt.xticks(arange(-Fs / 20, Fs / 20, step=20))  
plt.title("Αμφίπλευρο φάσμα πλάτους")
plt.xlabel("<- Συχνότητα ->")
plt.ylabel("Πλάτος ->")

plt.subplot(2, 1, 2)
mono_frequencies, monopleyro = mono_fasma(our_signal,t)   # Υπολογιστμός κεντραρισμένου Μονόπλευρου φάσμα πλάτους
plt.plot(mono_frequencies, monopleyro)
plt.ylim(0, 0.2)
plt.xlim(-Fs / 20, Fs / 20)
plt.xticks(arange(-Fs / 20, Fs / 20, step=20))   
plt.title("Μονόπλευρο φάσμα πλάτους")
plt.xlabel("<- Συχνότητα ->")
plt.ylabel("Πλάτος ->")
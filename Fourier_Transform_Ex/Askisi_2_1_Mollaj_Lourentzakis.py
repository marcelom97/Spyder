#%%
from fft_modules import amfi_fasma, mono_fasma
from numpy import pi, cos, linspace, abs
import matplotlib.pyplot as plt

A = 4
f = 10                                  #συχνότητα
T = 1 / f                               #περίοδος
B = f                               
Nyquist_Freq = 2 * B                    #ελάχιστη συχνότητα δειγματοληψίας (Nyquist frequency)
number_of_signal_periods = 5            #αριθμός περιόδων του σήματος
Tmax = number_of_signal_periods * T     #Συνολική χρονική διάρκεια του σήματος
samples_per_period = 1000               #αριθμός δειγμάτων ανά περίοδο
Ts = T / samples_per_period             #Χρόνος δειγματοληψίας
Fs = 1 / Ts                             #συχνότητα δειγματοληψίας (=samples_per_period*f)
t = linspace (0, Tmax, Tmax / Ts)  		#πίνακας χρόνου
total_samples = len(t)                  #συνολικός αριθμός δειγμάτων που θα ληφθούν κατά την διάρκεια του σήματος
 
my_signal = A * cos(2 * pi * f * t)     #συνημιτονικό σήμα 

plt.figure(1)                           #εικόνα 1
plt.plot(t, my_signal)                  #ζωγραφίζω το συνημιτονικό σήμα
plt.grid(axis="both")                   #βάζει γραμμές και στους 2 άξονες
plt.title("Συνημιτονικό σήμα")                   
plt.ylabel("Πλάτος ->")
plt.xlabel("Xρόνος ->")

plt.figure(2)

amfi_frequencies, amfipleyro = amfi_fasma(my_signal,t) # Υπολογιστμός κεντραρισμένου Αμφίπλευρου φάσμα πλάτους
plt.subplot(2, 1, 1)                    # Πάνω subplot
plt.plot(amfi_frequencies, amfipleyro)  
plt.ylim(0, 2 * A)
plt.xlim(-5 * B, 5 * B)                 # απο -50Hz έως 50Hz
plt.title("Αμφίπλευρο φάσμα πλάτους")
plt.xlabel("<- Συχνότητα ->")
plt.ylabel("Πλάτος ->")

mono_frequencies, monopleyro = mono_fasma(my_signal,t) # Υπολογιστμός κεντραρισμένου Mονόπλευρου φάσμα πλάτους
plt.subplot(2, 1, 2)                    # Κάτω subplot
plt.plot(mono_frequencies, monopleyro)
plt.ylim(0, 2 * A)                      
plt.xlim(-5 * B, 5 * B)                 # απο -50Hz έως 50Hz
plt.title("Mονόπλευρο φάσμα πλάτους")
plt.xlabel("<- Συχνότητα ->")
plt.ylabel("Πλάτος ->")

esd = abs(monopleyro)**2                # Μέτρο μετασχηματισμού fourier στο τετράγωνο ειναι η ενεργειακή φασματική πυκνότητα                 
print("Ενεργειακή φασματική πυκνότητα:"+str(max(esd)))
plt.figure(3)                           
plt.plot(mono_frequencies, esd)              
plt.xlim(0, 5 * B)                      # απο 0Hz έως 50Hz               
plt.ylim(0, A**2 + 4)
plt.ylabel("Πλάτος ->")
plt.xlabel("<- Συχνότητα ->")
plt.title("Ενεργειακή φασματική πυκνότητα")
#%%
from numpy import pi, linspace, sin
from scipy import signal
import matplotlib.pyplot as plt

T = 1                                                           #Περίοδος
f = 1 / T                                                       #Συχνότητα
t = linspace(-2, 2, 4000)                                       #Αρχικοποιώ πίνακα χρόνου

our_signal = signal.square(2 * pi * f * t)                      #Τετραγωνικός Παλμός

fourier_signal = linspace(0, 0, 4000)                           #Αρχικοποιώ πίνακα για την Σειρά Fourier
harmonic = linspace(0, 0, 4000)                                 #Αρχικοποιώ πίνακα για τις αρμονικές

number_of_armonics = int(input("Δωσε αριθμό αρμονικών:"))      #Διαβάζω πόσες αρμονικές θέλω
plt.figure(1) 
plt.plot(t, our_signal, label = "Τετραγωνικός παλμός")
plt.title("Τετραγωνικός παλμός με σήμα σειράς Fourier")
plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")

for n in range(1, number_of_armonics + 2, 2):                  #Για κάθε μια απο τις αρμονικές προσθέτω τις τιμές της
    fourier_signal += (4 / (n * pi)) * sin(2 * pi * f *n * t)   #σειράς Fourier στον πίνακα 
plt.plot(t, fourier_signal, label = "Σειρά Fourier")

plt.figure(2)
plt.title("Αρμονικές")
plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")

for n in range(1, number_of_armonics + 2, 2):                  #Στον πίνακα harmonic παίρνω μια μια τις αρμονικές και 
    harmonic = (4 / (n * pi)) * sin(2 * pi * f *n * t)          #τις κάνω plot
    plt.plot(t, harmonic)
    
failure = our_signal - fourier_signal                           #Η Διαφορά πλάτους του τετραγωνικού παλμού
                                                                #με το σήμα της σειράς Fourier
plt.figure(3)
plt.title("Σφάλμα")
plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")
plt.plot(t, failure)

plt.figure(4)
plt.title("Πλάτοι των αρμονικών")
plt.ylabel("Πλάτος")
plt.xlabel("Αρμονική")

for n in range(1, number_of_armonics + 2, 2):                 #Για κάθε μια απο τις αρμονικές παίρνω το πλάτος της και 
    A = (4 / (n * pi))                                         #το βάζω σε μια μεταβλητή Α 
    plt.scatter(n, A, s=20)                                    #Με την scatter εμφανίζω σε όποιο σημείο θέ΄λω μια τελεία
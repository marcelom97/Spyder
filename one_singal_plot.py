#%%
from numpy import pi, linspace, sin, cos
import matplotlib.pyplot as plt 

A = 5                               #Πλάτος του σήματος
f = 1000.0                          #Συχνότητα του σήματος
T = 1 / f                           #Περίοδος του σήματος
B = f                               #Εύρος ζώνης του σήματος
Nyquist_Fs = 2 * B                  #Ελάχιστη συχνότητα δειγματοληψίας - Κριτήριο Nyquist (παράγει δύο δείγματα ανά περίοδο του σήματος)
Multiples_Of_Nyquist_Frequensy = 10 #Για να βγάλω το sin σωστό βαζω 10 φορές την συχνότητα Niquist
                                    #Έχοντας κατά νού την ελάχιστη συχνότητα δειγματοληψίας θα μπορούσαμε να δειγματοληπτήσουμε το σήμα με συχνότητα 
                                    #μεγαλύτερη από αυτήν αλλάζοντας το 2 στην παραπάνω σχέση, πράγμα το οποίο θα μπορούσε να είναι και μεταβλητό με 
                                    #χρήση της συνάρτησης input π.χ:
                                    #Multiples_Of_Nyquist_Frequensy=int(input("Δώστε τον αριθμό των πολλααπλασίων της συχνότητας Nyquist >2))
                                    #αλλάζοντας την τιμή "1" παραπάνω αλλάζουμε και τον αριθμό των δειγμάτων που θα ληφθούν

our_sample_rate = Multiples_Of_Nyquist_Frequensy * Nyquist_Fs

Ts = 1 / Nyquist_Fs                 # ελάχιστη περίοδος δειγματοληψίας - Κριτήριο Nyquist
our_Ts = 1 / our_sample_rate

Tmax = 3 * T                        # Τρείς περίοδοι του σήματος θα σχεδιαστούν - Αυτό μπορεί να είναι και μεταβλητο και 
                                    # να ζητείται μέσω της input συνάρτησης π.χ.: 
                                    # number_of_periods=int(input("Δώστε το αριθμό των περιόδων που θέλετε να σχεδιαστούν))
                                    # Τmax=number_of_periods*T

samples_per_period = T / our_Ts     # αριθμός δειγμάτων ανά περίοδο
sample_points = samples_per_period * (Tmax / T) # συνολικός αριθμός δειγμάτων κατά την Τmax διάρκεια του σήματος

print("samples_per_period = " + str(samples_per_period)) 

t = linspace(0, Tmax, sample_points + 1,endpoint = True) # Από 0 ως Τmax λαμβάνονται κατά Τs sample_points+1 (συμπεριλαμβανομένου και του σημείου για t=0)

our_signal = A * sin(2 * pi * f * t) # Tο σήμα που έχουμε ορίσει με τις παραπάνω μεταβλητές

plt.figure(1)
plt.plot(t, our_signal)

plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")

plt.ylim(-6, 6)
plt.xlim(0, Tmax)
plt.stem(t, our_signal)
# plt.show()
# %%

from numpy import pi, linspace, sin, cos
import matplotlib.pyplot as plt

# ΠΕΡΙΣΣΟΤΕΡΑ ΤΟΥ ΕΝΟΣ ΣΗΜΑΤΑ
# Αν έχουμε περισσότερα του ενός σήματα, τότε θα δειγματοληπτήσουμε εφορμόζοντας το κριτήριο του Nyquist για το
# σήμα με την μεγαλύτερη συχνότητα και ο πίνακας του χρόνου θα είναι κοινός για όλα τα σήματα
# ακολουθεί παράδειγμα με πρόσθεση δύο σημάτων:
# ένα ημιτονικό πλάτους 5 και συχνότητας 1000Hz : Signal_1=5*sin(2*pi*1000*t)
# και ένα συνημιτονικό πλάτους 4 και συχνότητας 3000Hz : Signal_2=4*cos(2*pi*3000*t)
A1 = 5
A2 = 4
f1 = 1000
f2 = 3000
T1 = 1/f1
T2 = 1/f2
f = max(f1, f2)  # μέγιστη συχνότητα του σύνθετου σήματος
T = max(T1, T2)  # Περίοδος του σύνθετου σήματος

B = f  # Εύρος ζώνης του σύνθετου σήματος
Nyquist_Fs = 2*B  # Ελάχιστη συχνότητα δειγματοληψίας - Κριτήριο Nyquist
# (παράγει δύο δείγματα ανά περίοδο του σήματος με την μεγαλύτερη συχνότητα στην προκειμένη περίπτωση)

# Τα υπόλοιπα είναι τα ίδια με τα Α, Β, Γ, αυτό που αλλάζει είναι το σήμα μας

# 10 δείγματα ανά περίοδο του σήματος με την μεγαλύτερη συχνότητα
Multiples_Of_Nyquist_Frequensy = 5
our_Sampling_rate = Multiples_Of_Nyquist_Frequensy*Nyquist_Fs
Ts = 1/Nyquist_Fs
our_Ts = 1/our_Sampling_rate

Tmax = 4*T  # θα αναπαραστήσουμε το σύνθετο σήμα για τέσσερις περιόδους του σήματος με την μικρότερη συχνότητα
# δηλαδή του σήματος με την μεγαλύτερη περίοδο που αποτελεί και την περίοδο του σύνθετου σήματος

samples_per_period = T/our_Ts
sample_points = samples_per_period*(Tmax/T)

t = linspace(0, Tmax, sample_points+1, endpoint=True)
Signal_1 = A1*sin(2*pi*f1*t)
Signal_2 = A2*cos(2*pi*f2*t)

our_signal = Signal_1 + Signal_2  # tο σύνθετο σήμα

plt.figure(1)

plt.subplot(3,1,1)
plt.ylim(-10, 10)
plt.axhline(y = 0, color="r")
plt.ylabel("Signal 1")
plt.plot(t, Signal_1)

plt.subplot(3,1,2)
plt.ylim(-10, 10)
plt.axhline(y = 0, color="r")
plt.ylabel("Signal 2")
plt.plot(Signal_2)

plt.subplot(3,1,3)
plt.ylim(-10, 10)
plt.axhline(y = 0, color="r")
plt.ylabel("Signal 1\nSignal 2")
plt.plot(our_signal)
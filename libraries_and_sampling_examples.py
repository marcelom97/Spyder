#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 02:06:11 2018

@author: admin

ΠΑΡΑΔΕΙΓΜΑΤΑ ΧΡΗΣΗΣ ΤΩΝ ΒΙΒΛΙΟΘΗΚΩΝ ΚΑΙ modules του Python, και ΠΑΡΑΔΕΙΓΜΑΤΑ ΑΝΑΠΑΡΑΣΤΑΣΗΣ ΚΑΙ ΔΕΙΓΜΑΤΟΛΗΨΙΑΣ ΣΗΜΑΤΩΝ
"""

# ΧΡΗΣΗ ΤΩΝ ΒΙΒΛΙΟΘΗΚΩΝ ΚΑΙ modules του Python

# Γίνεται import μόνο των απαραίτητων modules και συναρτήσεων για το παρόν παράδειγμα
import numpy as np # θα μπορούσε και να παραληφθεί αυτή η εντολή εφόσον υπάρχει η επόμενη παρακάτω
from numpy import pi, linspace, sin, cos
import matplotlib.pyplot as plt

# Σχόλια για τις παραπάνω εντολές:
# Για να δείτε τις συναρτήσεις π.χ. της numpy δώστε στο Ipython console διαδοχικά τις εντολές: 
# import numpy
# dir(numpy)
# Για να πάρετε βοήθεια για κάποιο module, π.χ. το ημίτονο (sin) μπορείτε είτε να γράψετε στο Ipython console (μετά τα import):
# help(numpy.sin)
# Επίσης μπορείτε να γράψετε στο παράθυρο Help με Source το Console και στο πλάισιο κειμένου που γράφει Object το παρακάτω:
# numpy.sin
# Αντίστοιχα ισχύοθν για όλες τις βιβλιοθήκες και modules του Python
# Παράδειγμα για την matplotlib.pyplot στο ΙPython console:
# import matplotlib.pyplot
# dir(matplotlib.pyplot)
# help(matplotlib.pyplot.subplot)


# ΠΑΡΑΔΕΙΓΜΑΤΑ ΔΕΙΓΜΑΤΟΛΗΨΙΑΣ ΚΑΙ ΔΙΔΙΑΣΤΑΤΗΣ ΑΝΑΠΑΡΑΣΤΑΣΗΣ ΣΗΜΑΤΩΝ 

# A) Δειγματοληψία με ρυθμό ίσο με τον ρυθμό Nyquist (2 δείγματα ανά περίοδο του σήματος)

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
                                
our_Sampling_rate = Multiples_Of_Nyquist_Frequensy * Nyquist_Fs
                            
Ts = 1 / Nyquist_Fs                 #ελάχιστη περίοδος δειγματοληψίας - Κριτήριο Nyquist
our_Ts = 1 / our_Sampling_rate

Tmax = 3 * T                        # Τρείς περίοδοι του σήματος θα σχεδιαστούν - Αυτό μπορεί να είναι και μεταβλητο και 
                                    # να ζητείται μέσω της input συνάρτησης π.χ.: 
                                    #number_of_periods=int(input("Δώστε το αριθμό των περιόδων που θέλετε να σχεδιαστούν))
                                    #Τmax=number_of_periods*T
 
samples_per_period = T / our_Ts     #αριθμός δειγμάτων ανά περίοδο
sample_points = samples_per_period * (Tmax / T) # συνολικός αριθμός δειγμάτων κατά την Τmax διάρκεια του σήματος

#
print("samples_per_period = " + str(samples_per_period)) #Τυπώνει τον αριθμό των δειγμάτων ανά περιόδο Τ

t = linspace(0, Tmax, sample_points + 1, endpoint = True) # Από 0 ως Τmax λαμβάνονται κατά Τs sample_points+1 (συμπεριλαμβανομένου και του σημείου για t=0)

our_signal = A * sin(2 * pi * f * t) #Tο σήμα που έχουμε ορίσει με τις παραπάνω μεταβλητές

plt.figure(1)
plt.plot(t,our_signal) 

plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")

plt.ylim(-6, 6)
plt.xlim(0, Tmax)
plt.stem(t,our_signal)
plt.show

# Β) Δειγματοληψία με ρυθμό ίσο με τον ρυθμό Nyquist*5 (2*5=10 δείγματα ανά περίοδο του σήματος)
# Ο ιδιος με τον παραπάνω κώδικα για 10 δείγματα ανά περίοδο

Multiples_Of_Nyquist_Frequensy=5 # αυτή η εντολή αλλάζει μόνο
our_Sampling_rate=Multiples_Of_Nyquist_Frequensy*Nyquist_Fs
Ts=1/Nyquist_Fs             
our_Ts=1/our_Sampling_rate
Tmax=3*T                    
samples_per_period=T/our_Ts
sample_points=samples_per_period*(Tmax/T) 

print("samples_per_period="+str(samples_per_period)) 

t = linspace(0, Tmax, sample_points+1, endpoint=True) 
our_signal = A*sin(2*pi*f*t) 
plt.figure(2)
plt.plot(t,our_signal) 

plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")

plt.ylim(-6, 6)
plt.xlim(0, Tmax)
plt.stem(t,our_signal)
plt.show

# Γ) Δειγματοληψία με ρυθμό ίσο με τον ρυθμό Nyquist*50 (2*50=100 δείγματα ανά περίοδο του σήματος)
# Ο ιδιος με τον παραπάνω κώδικα για 100 δείγματα ανά περίοδο

Multiples_Of_Nyquist_Frequensy=50 # αυτή η εντολή αλλάζει μόνο
our_Sampling_rate=Multiples_Of_Nyquist_Frequensy*Nyquist_Fs
Ts=1/Nyquist_Fs             
our_Ts=1/our_Sampling_rate
Tmax=3*T                    
samples_per_period=T/our_Ts
sample_points=samples_per_period*(Tmax/T) 

print("samples_per_period="+str(samples_per_period)) 

t = linspace(0, Tmax, sample_points+1, endpoint=True) 
our_signal = A*sin(2*pi*f*t) 
plt.figure(3)
plt.plot(t,our_signal) 

plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")

plt.ylim(-6, 6)
plt.xlim(0, Tmax)
plt.stem(t,our_signal)
plt.show

# Δ)ΠΕΡΙΣΣΟΤΕΡΑ ΤΟΥ ΕΝΟΣ ΣΗΜΑΤΑ
# Αν έχουμε περισσότερα του ενός σήματα, τότε θα δειγματοληπτήσουμε εφορμόζοντας το κριτήριο του Nyquist για το 
# σήμα με την μεγαλύτερη συχνότητα και ο πίνακας του χρόνου θα είναι κοινός για όλα τα σήματα
# ακολουθεί παράδειγμα με πρόσθεση δύο σημάτων:
# ένα ημιτονικό πλάτους 5 και συχνότητας 1000Hz : Signal_1=5*sin(2*pi*1000*t)
# και ένα συνημιτονικό πλάτους 4 και συχνότητας 3000Hz : Signal_2=4*cos(2*pi*3000*t)
A1=5
A2=4
f1=1000
f2=3000
T1=1/f1
T2=1/f2
f=max(f1,f2) #μέγιστη συχνότητα του σύνθετου σήματος
T=max(T1,T2) #Περίοδος του σύνθετου σήματος

B=f                         #Εύρος ζώνης του σύνθετου σήματος
Nyquist_Fs=2*B              #Ελάχιστη συχνότητα δειγματοληψίας - Κριτήριο Nyquist 
                            #(παράγει δύο δείγματα ανά περίοδο του σήματος με την μεγαλύτερη συχνότητα στην προκειμένη περίπτωση)

# Τα υπόλοιπα είναι τα ίδια με τα Α, Β, Γ, αυτό που αλλάζει είναι το σήμα μας

Multiples_Of_Nyquist_Frequensy=5 # 10 δείγματα ανά περίοδο του σήματος με την μεγαλύτερη συχνότητα
our_Sampling_rate=Multiples_Of_Nyquist_Frequensy*Nyquist_Fs
Ts=1/Nyquist_Fs             
our_Ts=1/our_Sampling_rate

Tmax=4*T    # θα αναπαραστήσουμε το σύνθετο σήμα για τέσσερις περιόδους του σήματος με την μικρότερη συχνότητα
            # δηλαδή του σήματος με την μεγαλύτερη περίοδο που αποτελεί και την περίοδο του σύνθετου σήματος  
                
samples_per_period=T/our_Ts
sample_points=samples_per_period*(Tmax/T) 

t = linspace(0, Tmax, sample_points+1, endpoint=True) 
Signal_1=A1*sin(2*pi*f1*t)
Signal_2=A2*cos(2*pi*f2*t)

our_signal = Signal_1+Signal_2 # tο σύνθετο σήμα

plt.figure(4)

plt.subplot(4,1,1) #χρήση της subplot
plt.plot(t,Signal_1) 
plt.stem(t,Signal_1)
plt.ylim(-10, 10)
plt.xlim(0, Tmax)
plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")
plt.axvline(x=T1) #χρήση της axvline για να ζωγραφιστεί κατακόρυφη γραμμή στο τέλος της πρώτης περιόδου του Signal_1 (T=1/1000)

plt.subplot(4,1,2) #χρήση της subplot
plt.plot(t,Signal_2) 
plt.stem(t,Signal_2)
plt.ylim(-10, 10)
plt.xlim(0, Tmax)
plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος")
plt.axvline(x=T2) #χρήση της axvline για να ζωγραφιστεί κατακόρυφη γραμμή στο τέλος της πρώτης περιόδου του Signal_2 (T=1/3000)

plt.subplot(4,1,3) #χρήση της subplot
plt.plot(t,our_signal)
plt.ylim(-10, 10)
plt.xlim(0, Tmax)
plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος") 

plt.subplot(4,1,4) #χρήση της subplot
plt.stem(t,our_signal)
plt.ylim(-10, 10)
plt.xlim(0, Tmax)
plt.stem(t,our_signal)
plt.ylabel("Πλάτος")
plt.xlabel("Χρόνος") 
plt.axvline(x=T)    #χρήση της axvline για να ζωγραφιστεί κατακόρυφη γραμμή στο τέλος της πρώτης περιόδου του σύνθετου σήματος
plt.axvline(x=2*T)  #χρήση της axvline για να ζωγραφιστεί κατακόρυφη γραμμή στο τέλος της δεύτερης περιόδου του σύνθετου σήματος
plt.axvline(x=3*T)  #χρήση της axvline για να ζωγραφιστεί κατακόρυφη γραμμή στο τέλος της τρίτης περιόδου του σύνθετου σήματος

plt.show
print("samples_per_period="+str(samples_per_period)) #Τα δείγματα ανά περίοδο του σήματος με την μικρότερη συχνότητα

#μπορείτε να το τρέξετε με χρήση του Run cell για να δείτε τα αποτελέσματα βήμα προς βήμα
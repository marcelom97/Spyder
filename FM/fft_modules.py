# -*- coding: utf-8 -*-
"""
Created on Mon May  7 21:10:11 2018

@author: admin
"""
from numpy import linspace
from scipy.fftpack import fft, fftshift, fftfreq


def amfipleyro_fasma(my_signal, t):
    """Υπολογίζει τις συχνότητες και τις τιμές του αμφίπλευρου μη κεντραρισμένου φάσματος πλάτους ενός σήματος.

    Η είσοδος είναι το σήμα στο πεδίου του χρόνου (my_signal) και ο πίνακας του χρόνου (t).
    Η συνάρτηση επιστρέφει τις συχνότητες (Frequency_Range) και τις αντίστοιχες τιμές 
    του αμφίπλευρου φάσματος πλάτους του σήματος (amfipleyro_fft).
    Για τον υπολογισμό των συχνοτήτων γίνεται χρήσση της scipy.fftpack.fftfreq
    (https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.fftfreq.html)
    και οι συχνότητες που παράγονται με την fftfreq μπαίνουν στον αντίστοιχο πίνακα συχνοτήτων (Frequency_Range) ως εξής:
    Πρώτα από το 0 ως την μέγιστη θετική συχνότητα=Fs/2 και μετά από την μέγιστη αρνητική ως την πρώτη αρνητική πρίν το μηδέν, 
    όπως ακριβώς κατατάσσει και η συνάρτηση fft τα αποτελέσματα της.

    Έτσι για την σχεδίαση του φάσματος πλάτους ενός σήματος δεν απαιτείται η χρήση της scipy.fftpack.fftshift

    """

    Ts = t[1]-t[0]  # χρόνος δειγματοληψίας
    total_samples = len(t)  # συνολικός αριθμός δειγμάτων
    amfipleyro_fft = abs(fft(my_signal))/(total_samples)  # κανονικοποιημένο αμφίπλευρο φάσμα σήματος, μή κεντραρσμένο
    Frequency_Range = fftfreq(total_samples, d=Ts)  # συχνότητες του παραπάνω φάσματος (μη κεντραρισμένες)

    return Frequency_Range, amfipleyro_fft


def monopleyro_fasma(my_signal, t):
    """Υπολογίζει τις θετικές συχνότητες και τις τιμές του θετικού τμήματος του φάσματος πλάτους (μονόπλευρο φάσμα) ενός σήματος.

    Η είσοδος είναι το σήμα στο πεδίου του χρόνου (my_signal) και ο πίνακας του χρόνου (t).
    Η συνάρτηση επιστρέφει τις θετικές συχνότητες (Positive_Frequencies) και τις αντίστοιχες τιμές 
    του μονόπλευρου φάσματος πλάτους του σήματος (monopleyro_fft).

    H συνάρτηση υπολογίζει πρώτα το αμφίπλευρο μη κενραρισμένο φάσμα πλάτους του σήματος (για να είναι ανεξάρτητη)
    και στη συνέχεια διπλασιάζει το πλάτος του φάσματος αυτού εκτός από την συνιστώσα στην συχνότητα f=0 
    για να ληφθεί το μονόπλευρο φάσμα πλάτους και οι θετικές συχνότητες.

    """
    # Υπολογισμός αμφίπλευρου φάσματος
    Ts = t[1]-t[0]  # χρόνος δειγματοληψίας
    total_samples = len(t)  # συνολικός αριθμός δειγμάτων
    amfipleyro_fft = abs(fft(my_signal))/(total_samples)  # κανονικοποιημένο αμφίπλευρο φάσμα σήματος, μή κεντραρσμένο
    Frequency_Range = fftfreq(total_samples, d=Ts)  # συχνότητες του παραπάνω φάσματος (μη κεντραρισμένες)

    # Υπολογισμός μονόπλευρου φάσματος
    monopleyro_fft = 2*amfipleyro_fft[0:int(len(t)/2)]
    # Επαναφορά της συνιστώσας στη συχνότητα f=0 στην κανονική της τιμή
    monopleyro_fft[0] = monopleyro_fft[0]/2
    # Θετικές συχνότητες του φάσματος
    Positive_Frequencies = Frequency_Range[0:int(len(t)/2)]

    return Positive_Frequencies, monopleyro_fft


def amfi_fasma(my_signal, t):
    """Υπολογίζει τις συχνότητες και τις τιμές του αμφίπλευρου κεντραρισμένου φάσματος πλάτους ενός σήματος.

    Η είσοδος είναι το σήμα στο πεδίου του χρόνου (my_signal) και ο πίνακας του χρόνου (t).
    Η συνάρτηση επιστρέφει τις συχνότητες (Frequency_Range) και τις αντίστοιχες τιμές 
    του κεντραρισμένου αμφίπλευρου φάσματος πλάτους του σήματος (amfipleyro_fft).

    """

    Ts = t[1]-t[0]  # χρόνος δειγματοληψίας
    total_samples = len(t)  # συνολικός αριθμός δειγμάτων
    FFT_of_my_signal = fft(my_signal)  # επίδραση της συνάρτησης fft
    Normalized_FFT_of_my_signal = abs(FFT_of_my_signal)/(total_samples)  # κανονικοποίηση ως πρός το πλάτος
    amfipleyro_fft = fftshift(Normalized_FFT_of_my_signal)  # κεντράρισμα φάσματος με χρήση της συνάρτησης fftshift

    # Υπολογισμός κεντραρισμένου πίνακα συχνοτήτων
    if total_samples % 2 == 0:
        k = linspace(-total_samples/2, total_samples/2-1, total_samples)            # Ο αριθμός των δειγμάτων είναι άρτιος
    else:
        k = linspace(-(total_samples-1)/2, (total_samples-1)/2, total_samples)      # Ο αριθμός των δειγμάτων είναι περιττός

    Duration = total_samples*Ts
    Frequency_Range = k*(1/Duration)

    return Frequency_Range, amfipleyro_fft


def mono_fasma(my_signal, t):
    """Υπολογίζει τις συχνότητες και τις τιμές του μονόπλευρου κεντραρισμένου φάσματος πλάτους ενός σήματος.

    Η είσοδος είναι το σήμα στο πεδίου του χρόνου (my_signal) και ο πίνακας του χρόνου (t).
    Η συνάρτηση επιστρέφει τις θετικές συχνότητες (Positive_Frequencies) και τις αντίστοιχες τιμές 
    του μονόπλευρου φάσματος πλάτους του σήματος (monopleyro_fft).

    H συνάρτηση υπολογίζει πρώτα το κεντραρισμένο αμφίπλευρο φάσμα πλάτους του σήματος (για να είναι ανεξάρτητη)
    και στη συνέχεια διπλασιάζει το πλάτος του φάσματος αυτού εκτός από την συνιστώσα στην συχνότητα f=0 
    για να ληφθεί το μονόπλευρο φάσμα πλάτους και οι θετικές συχνότητες.

    """

    Ts = t[1]-t[0]  # χρόνος δειγματοληψίας
    total_samples = len(t)  # συνολικός αριθμός δειγμάτων
    FFT_of_my_signal = fft(my_signal)  # επίδραση της συνάρτησης fft
    Normalized_FFT_of_my_signal = abs(FFT_of_my_signal)/(total_samples)  # κανονικοποίηση ως πρός το πλάτος
    amfipleyro_fft = fftshift(Normalized_FFT_of_my_signal)  # κεντράρισμα φάσματος με χρήση της συνάρτησης fftshift

    # Υπολογισμός κεντραρισμένου πίνακα συχνοτήτων
    if total_samples % 2 == 0:
        k = linspace(-total_samples/2, total_samples/2-1, total_samples)            # Ο αριθμός των δειγμάτων είναι άρτιος
    else:
        k = linspace(-(total_samples-1)/2, (total_samples-1)/2, total_samples)      # Ο αριθμός των δειγμάτων είναι περιττός

    Duration = total_samples*Ts
    Frequency_Range = k*(1/Duration)

    # Υπολογισμός μονόπλευρου φάσματος
    monopleyro_fft = 2*amfipleyro_fft
    # Επαναφορά της συνιστώσας στη συχνότητα f=0 στην κανονική της τιμή
    monopleyro_fft[0] = monopleyro_fft[0]/2
    # Θετικές συχνότητες του φάσματος
    Positive_Frequencies = Frequency_Range[int(len(Frequency_Range)/2):int(len(Frequency_Range))]
    new_monopleyro_fft = monopleyro_fft[int(len(monopleyro_fft)/2):int(len(monopleyro_fft))]

    return Positive_Frequencies, new_monopleyro_fft

import pywhatkit

number_of_times = 999
time_in_minutes = 35
time_change = 1

tiem_send = time_in_minutes + time_change

for i in range(number_of_times):
    pywhatkit.sendwhatmsg('+65 9165 5655', 'I will send u to jesus', 12, tiem_send)

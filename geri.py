import time

def countdown(minute):
    saniye = minute*60
    while (0<saniye):
        new_minute = saniye
        mins, secs = divmod(new_minute, 60)
        timeformat = ("{:02d}:{:02d}".format(mins, secs))
        print(timeformat)
        time.sleep(1)
        saniye=saniye-1 
        
    print("Goodbye!nnnnn")

dakika= int(input("Dakika Girin:"))

countdown(dakika)
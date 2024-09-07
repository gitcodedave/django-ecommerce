import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) # divides t (in seconds) by 60 for mins and remainder secs
        timer = f'{mins:02d}:{secs:02d}' # fancy way to format the variables to the format: 2 digits filled with 0's to the left if needed
        print(timer, end='\r') # the end parameter with \r overwrites the preview line
        time.sleep(1)
        t -= 1

    print("Time's up!")

countdown(10)
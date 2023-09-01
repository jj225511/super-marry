import time

focus_time = 25 * 60 # Focus time in seconds (25 minutes)
break_time = 5 * 60 # Break time in seconds (5 minutes)

cycles = 4 # Number of cycles

for i in range(cycles):
    print(f"Focus time! {focus_time//60}:{focus_time%60:02d}")
    
    focus_timer = focus_time
    while focus_timer > 0:
        mins, secs = divmod(focus_timer, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        focus_timer -= 1
        
    print(f"\nBreak time! {break_time//60}:{break_time%60:02d}")
    
    break_timer = break_time
    while break_timer > 0:
        mins, secs = divmod(break_timer, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        break_timer -= 1
        
print("\nFocus timer finished!")

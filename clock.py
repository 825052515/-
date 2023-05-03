import time

def focus_timer(minutes):
    """ A function to create a focus timer for a specified number of minutes"""
    
    seconds = minutes * 60 # convert minutes to seconds
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        print("Focus! Time remaining: {} seconds".format(remaining_seconds))
        time.sleep(1)
        
    print("Well done! You focused for {} minutes.".format(minutes))


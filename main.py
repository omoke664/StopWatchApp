import time 

def stopWatch():
    input('Press Enter to start the stopwatch')
    start_time = time.time()
    print('Stopwatch started. Press Ctrl+C to stop.')
    
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            
            
            #Formating Time
            time_str = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            print(time_str, end= '\r') #Print over the same line
            
            time.sleep(1) #Update every second
            
            
    except KeyboardInterrupt:
        print('\nStopwatch stopped.')
        
        end_time = time.time()
        total_time = end_time - start_time
        print('Total elapsed time: {:.2f} seconds'.format(total_time))
        
if __name__ == '__main__':
    stopWatch()
    
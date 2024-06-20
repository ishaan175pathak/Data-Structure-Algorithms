from time import time 
def compute_average(n):
    """
    Performing n append to an empty list and return average time elapsed
    """
    data = []
    start = time()                  # recording the starting time of the appending item 
    for k in range(n):
        data.append(None)
    end = time()                    # recording the ending time of the appending item
    print(start,end)                # noting the starting and ending time
    return (end-start) / n          # returning the average time

alpha = compute_average(10000)

print(alpha)
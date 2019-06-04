# From https://mikulskibartosz.name/how-to-display-a-progress-bar-in-jupyter-notebook-47bd4c2944bf

import time, sys
from IPython.display import clear_output
def update_progress(progress):
    bar_length = 20
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1

    block = int(round(bar_length * progress))
    clear_output(wait = True)
    text = "Progress: [{0}] {1:.1f}%".format( "#" * block + "-" * (bar_length - block), progress * 100)
    
    print(text)
    
number_of_elements = 1000
for i in range(number_of_elements):
    time.sleep(0.1) #Replace this with a real computation
    update_progress(i / number_of_elements)
update_progress(1)

"""
Output:
Progress: [#####---------------] 23.3%
"""

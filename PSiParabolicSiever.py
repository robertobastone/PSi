################################################### PSi parabolic siever

# author: Roberto Bastone
# email: robertobastone93@gmail.com

version = 1.00

################################################### Packages

import numpy as np
import matplotlib.pyplot as plt

################################################### Packages

class PSiParabolicSiever:
    
    def __init__(self):
        print "Initializing...PSiParabolicSiever version " + str(version)
        
    def siever(self):
        frame = 7                            # size of plot
        integer = int(raw_input(">Choose how many integers to display: "))
        integer_for_plotting =  np.ceil(np.sqrt(integer))
        rightIntegers = np.linspace(2,integer,integer-1)
        leftIntegers = rightIntegers * -1
        wholeIntegers = np.concatenate((leftIntegers,rightIntegers),axis=None)
        x_parabola = np.linspace(-integer_for_plotting*2,integer_for_plotting*2,1001)
        # settings for the plot
        fig = plt.figure(figsize=(frame,frame))
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.set_xlim(-integer_for_plotting-1,integer_for_plotting+1)
        ax.set_ylim(0,integer)
        ax.set_yticks(np.linspace(1,integer,integer))
        # plotting
        plt.scatter(wholeIntegers,wholeIntegers**2, color='red',zorder=10)
        plt.plot(x_parabola,x_parabola**2)
        self.ParabolicSieve(leftIntegers,rightIntegers)          
        plt.show()           
        
    def ParabolicSieve(self,leftIntegers,rightIntegers):
        for i in range (0,len(leftIntegers)):
            for j in range (0,len(rightIntegers)):
                plt.plot( (leftIntegers[i], rightIntegers[j] ), (leftIntegers[i]**2, rightIntegers[j]**2 ), color='black', linewidth =0.5)
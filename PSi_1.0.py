################################################### FiLS

# author: Roberto Bastone
# email: robertobastone93@gmail.com

version = 1.0

################################################### Packages

import numpy as np
import matplotlib.pyplot as plt

################################################### INTRODUCTION

print ">Welcome to the Prime Siever (PSi) version ", version 
yes = {'Y','y'}
no = {'N','n'}

while True:
    choice = raw_input(">PSi provides several sieves. Do you want me to print a list of? [y/n] \n").lower()
    if choice in yes:
	print ">1) By typing \"parabolic\", PSi will use the parabolic sieve by Matiyasevich and Stechkin;"
        #print ">2) By choosing \"sum\", FiLS will calculate the sum of the first n terms of the sequence;"
        #print ">3) By selecting \"gold\", FiLS will output the ratios of the adjacent terms for the first n terms of the sequence and, as well, produce a plot showing how it varies;"
        #print ">4) By typing \"sunflower\", FiLS will 4reproduce the sunflower seed pattern that presents spirals following the Fibonacci sequence;" 
	#print ">5) By choosing \"spiral\". FiLS will plot a Fibonacci-like spiral. \n "
        break
    elif choice in no:
        print">Okay, let us continue"
        break
    else:
        print(">Please, select [y/n] only")
        continue

frame = 7                            # size of plot

while True:
	fnct = raw_input(">What sieve do you choose? ").lower()
	if ( fnct == "parabolic"):			#fib function
		integer = int(raw_input(">Choose how many integers to display: "))
         	integer_for_plotting =  np.ceil(np.sqrt(integer))
		rightIntegers = np.linspace(2,integer,integer-1)
		leftIntegers = rightIntegers * -1
                wholeIntegers = np.concatenate((leftIntegers,rightIntegers),axis=None)
		x_parabola = np.linspace(-integer_for_plotting*2,integer_for_plotting*2,1001)
		def ParabolicSieve(no_variable):
    			for i in range (0,len(leftIntegers)):
                  		for j in range (0,len(rightIntegers)):
                   			plt.plot( (leftIntegers[i], rightIntegers[j] ), (leftIntegers[i]**2, rightIntegers[j]**2 ), color='black', linewidth =0.5)
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
		ParabolicSieve(0)          
		plt.show()           
		break
	else:
	        print(">Error! Type a valide entry")
	        continue


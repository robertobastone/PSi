################################################### PSI

# author: Roberto Bastone
# email: robertobastone93@gmail.com

version = 1.01

################################################### IMPORT

import PSiParabolicSiever as PPS
from termcolor import colored

################################################### CLASS
class PrimeSiever:
    yes = {'Y','y','YES','yes','Yes'}
    no = {'N','n','NO','no','No'}

    #### INITIALIZING
    def __init__(self):
        print colored("Initializing... PrimeSiever version " + str(version), 'blue')
    #### INITIALIZING        
    def main(self):
        self.introduction(self.yes,self.no)
        self.sievesChoice()
    ### INTRODUCTION
    def introduction(self,yes,no):
        while True:
            choice = raw_input(">PSi provides several sieves. Do you want me to print a list of? [y/n] \n").lower()
            if choice in yes:
                print ">1) By typing \"parabolic\", PSi will use the parabolic sieve by Matiyasevich and Stechkin;"
                print ">2) Typing \"quit\" will terminate the execution of the script;"
                break
            elif choice in no:
                print">Okay, let us continue"
                break
            else:
                print( colored(">Please, select [y/n] only",'yellow'))
                continue
    ### SIEVES CHOICE
    def sievesChoice(self):
        while True:
            fnct = raw_input(">What sieve do you choose? ").lower()
            if ( fnct == "parabolic"):
                parabolic = PPS.PSiParabolicSiever()
                parabolic.siever()
            elif( fnct == "quit"):
                print colored("Terminating... PrimeSiever version " + str(version),'blue')
                break
            else:
                print( colored('>Error! Type a valide entry','red'))
                continue
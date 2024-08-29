"""
SIR MODEL 

"""

import numpy as np  
from ODESOLVER import ForwardEuler
from matplotlib import pyplot as plt

class SIR : 
    def __init__(self , nu , beta , S0 , I0 , R0) : 
        """
        nu , beta : parameters in the ODE system 
        S0 , I0 , R0 Are initial values

        """
        if(  isinstance(  nu , (float , int)  )) : 
            # Is number ? 
            self.nu = lambda t : nu 
        elif callable(nu) : 
            self.nu = nu 

        if(  isinstance(  beta , (float , int)  )) : 
            # Is number ? 
            self.beta = lambda t : beta
        elif callable(beta) : 
            self.beta = beta 
        
        self.initial_conditions = [S0, I0 , R0 ]

    def __call__( self , u , t ) : 
        S , I , _ = u 
        return np.asarray([
            -self.beta(t)*S*I ,#Succeptable 
            self.beta(t)*S*I - self.nu(t)*I ,  #Infected 
            self.nu(t)*I # Recovered 
        ])


if __name__ ==  "__main__" : 

    # beta  = lambda t : 0.004 if( t%2==0 ) else 0.0007

    sir = SIR(0.1 , 0.0004 , 1500 , 1 , 0 ) 
    solver = ForwardEuler(sir) 
    solver.set_initial_conditions(sir.initial_conditions) 

    time_steps  = np.linspace( 0 , 60 , 10001 ) 
    u , t = solver.solve( time_steps )
    print(u)
    plt.plot( t , u[ : ,0] , label = "Succeptible" ) 
    plt.plot( t , u[ : ,1] , label = "Infected" ) 
    plt.plot( t , u[ : ,2] , label = "Recovered" ) 
    plt.legend( ) 
    plt.show( ) 




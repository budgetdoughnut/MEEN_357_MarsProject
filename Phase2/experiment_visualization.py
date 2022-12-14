
import numpy as np
from scipy.interpolate import interp1d
from define_experiment import experiment1
import matplotlib.pyplot as plt

def visualize_terrain():
    experiment = experiment1()[0]
        
    alpha_fun = interp1d(experiment['alpha_dist'], experiment['alpha_deg'], kind = 'cubic', fill_value= 'extrapolate') #cubic interpolation between the points in alphadeg as a function of alphadist
        
    x = np.linspace(experiment['alpha_dist'][0], experiment['alpha_dist'][-1], 101) #100 position points between first and last value of dist
    
    plt.plot(experiment['alpha_dist'], experiment['alpha_deg'],'r*', x, alpha_fun(x)) #plotting
    plt.xlabel('Terrain Position (m)')
    plt.ylabel('Terrain Angle (deg)')
    plt.title('Terrain Angle vs Terrain Position')
    
visualize_terrain()
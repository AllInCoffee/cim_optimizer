# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:26:02 2024

@author: yanxi
"""

import sys
from pathlib import Path
sys.path.append(str(Path.cwd()) + "\\..\\") # append repo to list of search directories 
print(Path.cwd())
from solve_Ising import *
from CIM_helper import brute_force

instance_path_str_MAXCUT = str(Path.cwd()) + "\\..\\instances\\MC_Instances_NPZ\\"

# 20 spin MAXCUT problem
N = 20
mc_id = 1 # select first example of 20 spin MAXCUT problem
J = - np.load(instance_path_str_MAXCUT + f"MC50_N={N}_{mc_id}.npz") # load J matrix for 50% density MAX-CUT problem
gamma = 0.010 # set gamma hyperparameter

spins_ground, E_ground = brute_force(J)
print("The spin configuration in the ground state is {}".format(spins_ground))
print("The ground energy is {}".format(E_ground))

print('-----------------------------------')
print('The results for solver with CAC: ')
test1 = Ising(J).solve(cac_gamma=gamma, hyperparameters_randomtune = False)
print(f'whether randomtune is on: {test1.hyperparameters_randomtune}.')
#print(np.shape(test1.result['spin_trajectories']))
test1.result.plot_spin_trajectories(plot_type="spins")
test1.result.plot_spin_trajectories(plot_type="energy")

print('-----------------------------------')
print('The results for solver with AHC: ')
test2 = Ising(J).solve(use_CAC = False, hyperparameters_randomtune = False)
test2.result.plot_spin_trajectories(plot_type="spins")
test1.result.plot_spin_trajectories(plot_type="energy")
# print(np.shape(test2.result['spin_trajectories']))
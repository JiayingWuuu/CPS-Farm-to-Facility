# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:12:08 2021

@author: gareyes3
"""
#%%
import sys, os
sys.path
#sys.path.append('C:\\Users\Gustavo Reyes\Documents\GitHubFiles\CPS-Farm-to-Facility\Model')
sys.path.append('C:\\Users\gareyes3\Documents\GitHub\CPS-Farm-to-Facility\Model')

# %%
from importlib import reload
import numpy as np
import Listz
import pandas as pd
import MainModel3z
import SCInputz
import Inputz
import ContCondz
import ScenCondz
import InFunz
import OutFunz
import ContScen
import Funz
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
import sys
import Trial_MainLoop_PH
sys.path
#sys.path.append('C:\\Users\Gustavo Reyes\Documents\GitHubFiles\CPS-Farm-to-Facility\Model')
sys.path.append(
    'C:\\Users\gareyes3\Documents\GitHub\CPS-Farm-to-Facility\Model')
#%%

#Scenarios Creation

# 1 CFU/g Contmination Level
One_CFU_g = 45400000 #CFUs

#Uniform Contmaination in the Field. 
# Contamination Challenges
ContCondz.Background_C = True
ContCondz.Point_Source_C =False
ContCondz.Systematic_C = False

# Harvester Contamination
ContCondz.Crew_C = False
ContCondz.Harvester_C = False

# Processing equipment
ContCondz.PE_C = False
ContCondz.PE_Cont_Loc = False,  # 1,2,3,4,5
# 1 = Shredder, #2 = Belt, #3 = Washing, #4 Shaker, #5Centrifuge
ContCondz.Pack_C = False


#%% Scenario 1. No intervention Strategies, Natural Field and No Washing. 
reload(SCInputz)  # Reload Inputz
reload(Listz)  # Reload Lists

# Turning of Washing. 
SCInputz.Washing_YN = False 
SCInputz.BGHazard_lvl = One_CFU_g

#Sampling Condition
# Sampling Conditions, Baseline all conditions are off
ScenCondz.Baseline_Sampling = 0  # all others must be 0if this one is 1
ScenCondz.PH_Sampling = 0
ScenCondz.H_Sampling = 0
ScenCondz.R_Sampling = 0
ScenCondz.FP_Sampling = 0
# Pre_Harvest 4 Days
ScenCondz.PHS_4d = 0  # Scenario 1
ScenCondz.PHS_4h = 0  # Scenario 2
ScenCondz.PHS_Int = 0  # Scenario 3


#Running The Model.
Main_Mod_Outs = MainModel3z.F_MainLoop()

#Getting the outputs from the function.
OutputDF = Main_Mod_Outs[1]
ProgDF = Main_Mod_Outs[0]

#Final Contmination Baseline Scenario
Final_CFU_Baseline =ProgDF["Final Product Facility"]

#Creating boxplot for exploration
plt.boxplot(Final_CFU_Baseline)
plt.ticklabel_format(style='plain', axis='y')

#Percent Reduction by System Initial vs Final
(One_CFU_g-Final_CFU_Baseline.mean())/One_CFU_g #Average Reduction. 


#%% Scenario 2. No Sampling, Only Intervention Strategy is Washing

reload(SCInputz)  # Reload Inputz
reload(Listz)  # Reload Lists

# Turning of Washing. 
SCInputz.Washing_YN = True
SCInputz.BGHazard_lvl = One_CFU_g

#Sampling Condition
# Sampling Conditions, Baseline all conditions are off
ScenCondz.Baseline_Sampling = 0  # all others must be 0if this one is 1
ScenCondz.PH_Sampling = 0
ScenCondz.H_Sampling = 0
ScenCondz.R_Sampling = 0
ScenCondz.FP_Sampling = 0
# Pre_Harvest 4 Days
ScenCondz.PHS_4d = 0  # Scenario 1
ScenCondz.PHS_4h = 0  # Scenario 2
ScenCondz.PHS_Int = 0  # Scenario 3


#Running The Model.
Main_Mod_Outs = MainModel3z.F_MainLoop()

#Getting the outputs from the function.
OutputDF_Base_Wash = Main_Mod_Outs[1]
ProgDF_Base_Wash = Main_Mod_Outs[0]

#Final Contmination Baseline Scenario
Final_CFU_Base_Wash =ProgDF_Base_Wash["Final Product Facility"]

#Creating boxplot for exploration
plt.boxplot(Final_CFU_Base_Wash)
plt.ticklabel_format(style='plain', axis='y')

#Percent Reduction by System Initial vs Final
(One_CFU_g-Final_CFU_Base_Wash.mean())/One_CFU_g #Average Reduction.

#%% Scenario 3 PH Sampling 4D, Washing off , and normal baseline contamination reduction
    #PH Sample: 1 Sample/Sublot, 
    #Rejection Rule: "Lot
    #Sample Mass: 365g per sublot
    # GRabs per Sublot = N60

reload(SCInputz)  # Reload Inputz
reload(Listz)  # Reload Lists

# Turning of Washing. 
SCInputz.Washing_YN = False
SCInputz.BGHazard_lvl = One_CFU_g

#Sampling Condition
# Sampling Conditions, Baseline all conditions are off
ScenCondz.Baseline_Sampling = 0  # all others must be 0if this one is 1
ScenCondz.PH_Sampling = 1
ScenCondz.H_Sampling = 0
ScenCondz.R_Sampling = 0
ScenCondz.FP_Sampling = 0
# Pre_Harvest 4 Days
ScenCondz.PHS_4d = 1  # Scenario 1
ScenCondz.PHS_4h = 0  # Scenario 2
ScenCondz.PHS_Int = 0  # Scenario 3
   
#Only on when sampling,
SCInputz.sample_size_PH = 375 # (Input) g #Sample Size in grams for Pre Harvest
SCInputz.n_samples_slot_PH = 1 # (Input) Samples per sublot of product
SCInputz.No_Grabs_PH = 60
SCInputz.Limit_PH = 0
SCInputz.RR_PH_Trad = "Lot" #Reject by Sublot


#Running The Model.
Main_Mod_Outs = MainModel3z.F_MainLoop()

#Getting the outputs from the function.
OutputDF_Base_PHS4d = Main_Mod_Outs[1]
ProgDF_Base_PHS4d = Main_Mod_Outs[0]

#Final Contmination Baseline Scenario
Final_CFU_Base_PHS4d =ProgDF_Base_PHS4d["Final Product Facility"]

#Creating boxplot for exploration
plt.boxplot(Final_CFU_Base_PHS4d)
plt.ticklabel_format(style='plain', axis='y')

#Percent Reduction by System Initial vs Final
(One_CFU_g-Final_CFU_Base_PHS4d.mean())/One_CFU_g #Average Reduction.

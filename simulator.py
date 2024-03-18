#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Store Coefficients to Dictionary
coefficients = pd.DataFrame({
    'Feature': ['A1_L2', 'A1_L1', 'A1_13', 'A1_Lo', 'A1_14', 'A1_19', 'A1_39', 'A1_33', 'A1_17', 'A1_35', 
                'A1_18', 'A1_34', 'A1_21', 'A1_24', 'A1_20', 'A1_25', 'A1_11', 'A1_L6', 'A1_36', 'A1_30', 
                'A1_28', 'A1_38', 'A1_27', 'A1_26', 'A1_31', 'A1_L7', 'A1_L8', 'A1_22', 'A1_L3', 'A1_L4', 
                'A1_16', 'A1_10', 'A1_L9', 'A1_23', 'A1_15', 'A1_37', 'A1_32', 'A1_12', 'A1_L5', 'A1_29'],
    'Coefficient': [0.152874, 0.147132, 0.112891, 0.108284, 0.106064, 0.084204, 0.066624, 0.063970, 0.063316, 
                    0.060135, 0.051598, 0.036614, 0.031319, 0.029004, 0.022114, 0.019915, 0.016628, 0.014507, 
                    0.000000, 0.000000, -0.000000, 0.000000, 0.000000, 0.000000, 0.000000, -0.000000, -0.000000, 
                    -0.000000, 0.000000, 0.000000, 0.000000, -0.000000, 0.000000, 0.000000, -0.015750, -0.026851, 
                    -0.028529, -0.032299, -0.064901, -0.086442]
})

def satisfaction_simulator(improvements):
    impact_percentage = 0
    for feature, improvement_percentage in improvements.items():
        coefficient = coefficients.loc[coefficients['Feature'] == feature, 'Coefficient'].values[0]
        impact_percentage += coefficient * improvement_percentage / 100
    return impact_percentage * 100


# In[2]:


# Example
improvements = {
    'A1_L2': 10,  
    'A1_L1': 5,   
    'A1_13': 8    
}

impact_percentage = satisfaction_simulator(improvements)
print(f"Overall satisfaction is expected to increase: {impact_percentage:.2f}%")


# In[ ]:





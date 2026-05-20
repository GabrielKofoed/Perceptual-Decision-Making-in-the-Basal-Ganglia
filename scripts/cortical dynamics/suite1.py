"""
For running the model across different levels of noise. Testing the performance with and without the cortex.
"""

from project.networks.cbgt import ModelParams, ThalamusParams, BGParams
from project.networks.cortex import CortexParams
from project.utilities.simulation import DotsParams, run_experiments, TrialParams
from project.utilities.io import save_results


# Parameters combinations to test. 
varying_params = {
    'coherence': [1, 0.3, 0.15, 0.1, 0.08, 0.05, 0.03, 0.01],
    'noise_std': [0.125, 0.25, 0.5]
}

# ---- Parameters -----
bg_params = BGParams()
thal_params = ThalamusParams()
cx_params = CortexParams()
model_parameters = ModelParams(
    bg_params = bg_params, 
    th_params = thal_params, 
    cx_params = cx_params
    )
base_params = DotsParams(
    direction = None, 
    strength = 1
    )
trial_params = TrialParams(
    model_seed = 1, 
    task_seed = 1, 
    t_warmup = 0.15, 
    decision_threshold = 0.7,
    decision_window= 5e-3,
    PD_window = 1,
    max_time = 1
    )

# --- Running Experiments ---
# With cortex
results = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params, 
    varying_params = varying_params, 
    trial_params = trial_params, 
    n_trials_per_exp = 100,
    return_trials = True,
    bypass_cortex = False
    )

# Bypass cortex
results_bypass = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params,
    varying_params = varying_params, 
    trial_params = trial_params, 
    n_trials_per_exp = 100, 
    return_trials = True,
    bypass_cortex = True
    )

save_results(results, 'suite1', 'data/cortical dynamics')
save_results(results_bypass, 'suite1_bypass', 'data/cortical dynamics')


"""
Simulations used to test the model across different model seeds, reproducing the results of suite 1
Running the model across different levels of noise.
"""

from project.networks.cbgt import ModelParams, ThalamusParams, BGParams
from project.networks.cortex import CortexParams
from project.utilities.simulation import DotsParams, run_experiments, TrialParams
from project.utilities.io import save_results
from dataclasses import replace 


# Parameters combinations to test. Testing for both different noise levels and 
varying_params = {
    'coherence': [1, 0.3, 0.15, 0.1, 0.08, 0.05, 0.03, 0.01],
    'noise_std': [0.125, 0.25, 0.5],
}

# ---- Parameters -----
model_seed = 2

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
    model_seed = model_seed, 
    task_seed = 1, 
    t_warmup = 0.15, 
    decision_threshold = 0.7,
    decision_window= 5e-3,
    PD_window = 1,
    max_time = 1
    )

# --- Running Experiments ---
# Model 2
results2 = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params, 
    varying_params = varying_params, 
    trial_params = trial_params, 
    n_trials_per_exp = 100,
    return_trials = True,
    bypass_cortex = False,
    )
# Model 3
results3 = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params, 
    varying_params = varying_params, 
    trial_params = replace(trial_params, model_seed = model_seed + 1),
    n_trials_per_exp = 100,
    return_trials = True,
    bypass_cortex = False,
    )
# Model  4
results4 = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params, 
    varying_params = varying_params, 
    trial_params = replace(trial_params, model_seed = model_seed + 2), 
    n_trials_per_exp = 100,
    return_trials = True,
    bypass_cortex = False,
    )




save_results(results2, 'suite5_2', 'data')
save_results(results3, 'suite5_3', 'data')
save_results(results4, 'suite5_4', 'data')

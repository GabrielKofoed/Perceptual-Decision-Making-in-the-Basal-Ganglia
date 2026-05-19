"""
Simulation the effect of learning on model performance by testing different relative contributions of direct and indirect pathways
Running the model across different noise realizations.
"""

from project.networks.cbgt import ModelParams, ThalamusParams, BGParams
from project.networks.cortex import CortexParams
from project.utilities.simulation import DotsParams, run_experiments, TrialParams
from project.utilities.io import save_results


# Parameters combinations to test. Testing for both different noise levels and 
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
# pathway_bias = -0.10
results_m10 = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params, 
    varying_params = varying_params, 
    trial_params = trial_params, 
    n_trials_per_exp = 100,
    return_trials = True,
    bypass_cortex = False,
    pathway_bias = -0.10
    )
# pathway_bias = 0.10
results_10 = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params, 
    varying_params = varying_params, 
    trial_params = trial_params, 
    n_trials_per_exp = 100,
    return_trials = True,
    bypass_cortex = False,
    pathway_bias = 0.10
    )
# pathway_bias = 0.20
results_20 = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params, 
    varying_params = varying_params, 
    trial_params = trial_params, 
    n_trials_per_exp = 100,
    return_trials = True,
    bypass_cortex = False,
    pathway_bias = 0.20
    )




save_results(results_m10, 'suite3_m10', 'data/learning')
save_results(results_10, 'suite3_10', 'data/learning')
save_results(results_20, 'suite3_20', 'data/learning')


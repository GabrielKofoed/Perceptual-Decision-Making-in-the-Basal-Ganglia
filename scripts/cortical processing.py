"""
To gain a better idea of the cortical processing effect, by testing minimum passing coherence without cortex for coherences between
0.3 and 1 for strengths 0.4 and 0.6.
"""

from project.networks.cbgt import ModelParams, ThalamusParams, BGParams
from project.networks.cortex import CortexParams
from project.utilities.simulation import DotsParams, run_experiments, TrialParams
from project.utilities.io import save_results


# Parameters combinations to test. 
varying_params = {
    'coherence': [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],
    'strength': [0.60, 0.40]
}

# ----- Parameters -----
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
    noise_std = 0.125
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

# Bypass cortex
results_bypass_SvC = run_experiments(
    model_params = model_parameters, 
    base_dots_params = base_params,
    varying_params = varying_params, 
    trial_params = trial_params, 
    n_trials_per_exp = 100, 
    bypass_cortex = True
    )

save_results(results_bypass_SvC, 'cortical_processing_SvC', 'data')


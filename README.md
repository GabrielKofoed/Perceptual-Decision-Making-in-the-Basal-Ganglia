# Perceptual decision making in the basal ganglia

This repository contains code for my bachelor project on a cortico-basal
ganglia-thalamic model for perceptual decision making, with a focus on possible
implementation in neuromorphic hardware.

The model is implemented in Python using Nengo and simulates a two-alternative
perceptual decision-making task inspired by random dot motion experiments.

## Academic context

This repository accompanies a bachelor project on basal-ganglia-inspired
perceptual decision making and neuromorphic hardware.

If reusing the code or ideas, please cite the associated thesis or contact the
author.

## Project overview

The project investigates the performance a basal ganglia-inspired action selection
circuit perceptual decision making under ambiguous sensory input. Furthermore,
it investigates whether a cortex-inspired pre-processing unit can improve performance,
and how global modulation of excitability through learning could affect the decision-making
process

The model consists of:

- a cortex-inspired preprocessing module
- a basal ganglia action-selection circuit
- a thalamic output stage
- simulation tools for testing accuracy, reaction time, and decision stability.

The task uses left/right stimulus inputs with varying strength, coherence, and
noise.

Furthermore, this repository contains the data and figures generated for the thesis.

## Usage
Download dependencies from requirements.txt and pyproject.toml. If pyproject.toml is not
incorporated correctly, the system will not be able to find the source files. The dependencies 
can be installed like this.
```bash
pip install -e .
pip install -r requirements.txt
```
If you are using visual studio code, I recommend creating a virtual envelope and specifying that
dependencies should be installed from the two mentioned files.

Look to the scripts folder if you want to reproduce data from the thesis. Look to the notebooks
if you want to reproduce the figures.
You can also run your own experiments. Study the networks carefully along with the simulation builder.

>[!CAUTION]
>The generated figures depend upon a working Tex installation, such as MikTex of TeX Live.
>The notebooks will not run if you do not have Tex installed. Alternatively, remove the line 
>`use_latex_fonts()` in the beginning of each notebook. I cannot guarantee that the plots
>will look pretty, however.
>Also, if you wish to reproduce data by using the given scripts, be aware that data generation
>will take a long time. Each script can take a few hours to complete. Alternatively, the amount
>of neurons per ensemble can be reduced.

## Repository structure

```text
data/ # Contains the data generated in this project
├── cortical dynamics/ # For testing the effect of the cortex on performance
├── learning/          # For testing the effects of global modulation on excitability
└── model realizations # For testing model performance for different seeds

figures/               # Figures generated for the thesis
notebooks/             # Exploratory notebooks, used for generating figures 
scipts/                # scipts for generating data

src/
├── networks/          # Model components
    ├── cbgt.py        # CBGT model builder
    └── cortex.py      # Cortex builder
└── utilities/         # Simulation builder, statistics, and helper functions
    ├── io.py          # Functions for saving data, loading data, and generating figures.
    ├── simulation.py  # Simulation builder. For running tasks and generating data
    └── statistics.py  # Helper functions for calculating statistics with confidence intervals

notebooks/           # Exploratory notebooks and figure generation
pyproject.toml       # Configuration. It allows src to be installed as a local package.
requirements.txt     # Python dependencies
README.md            # Project description
LICENSE              # Repository license
```

## References
### Nengo and the Neural Engineering Framework
Applied Brain Research. Nengo API Reference. https://www.nengo.ai/nengo/v4.0.0/networks.html#nengo.networks.Thalamus. Accessed 20 May 2026

Eliasmith, C. (2013). *How to Build a Brain: A Neural Architecture for Biological Cognition*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199794546.001.0001

Stewart, T. C. (2012). *A technical overview of the Neural Engineering Framework* (Technical Report). Centre for Theoretical Neuroscience. Extended version of an article for *AISB Quarterly: The Newsletter of the Society for the Study of Artificial Intelligence and Simulation of Behaviour*, Issue 135.

Stewart, T. C., Tripp, B., & Eliasmith, C. (2009). *Python scripting in the Nengo simulator*. Frontiers in Neuroinformatics, 3. https://doi.org/10.3389/neuro.11.007.2009

### CBGT models
Xiao-Jing Wang. *Probabilistic decision making by slow reverberation in cortical circuits*. In: Neuron 36 (2002), pp. 955–968. doi: 10.1016/S0896-6273(02)01092-9.

Ding, L., & Gold, J. I. (2013). *The basal ganglia’s contributions to perceptual decision making*. Neuron, 79, 640–649. https://doi.org/10.1016/j.neuron.2013.07.042

Dunovan, K., Vich, C., Clapp, M., Verstynen, T., & Rubin, J. (2019). *Reward-driven changes in striatal pathway competition shape evidence evaluation in decision-making*. PLOS Computational Biology, 15(5), e1006998. https://doi.org/10.1371/journal.pcbi.1006998

Wei, W., Rubin, J. E., & Wang, X.-J. (2015). *Role of the indirect pathway of the basal ganglia in perceptual decision making*. Journal of Neuroscience, 35(9), 4052–4064. https://doi.org/10.1523/JNEUROSCI.3611-14.2015


### The dots task
Wulfram Gerstner et al. *Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition*. 2014.
Perceptual Decision Making Exercise (Python)url: https://neuronaldynamics-exercises.readthedocs.io/en/latest/exercises/perceptual-decision-making.html
Accessed 6 April 2026

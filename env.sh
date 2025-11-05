module load miniconda
conda create -p $(pwd)/conda_env python=3.10 jupyterlab notebook bash_kernel nvidia/label/cuda-12.8.1::cuda-toolkit  numpy scipy matplotlib pandas plotly
conda activate /gpfs/radev/home/pl543/project/git-sources/training/misha-2025-fall/conda_env

pip install torch torchvision

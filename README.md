# PYTEST
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

This respository demonstrates the unit test and integration testing using Pytest for Data Science Applications.

## Environment setup

All Python packages necessary to run the code in this repository are listed in `CostOfLiving/requirements.txt`. To create a new Anaconda environment which includes these packages, enter the following command in your terminal:

```bash
conda create --name ds_unit_testing --file CostOfLiving/requirements.txt
conda activate ds_unit_testing
```

## Running unit tests

To run the unit tests, simply run pytest in the CostOfLiving directory.

```bash
cd CostOfLiving
pytest
```

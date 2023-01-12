# Edda-MLDP

A difficulty rank predictor for Ragnarock maps powered by machine learning.

## Requirements

- Python 3
  - numpy
  - scikit-learn
  - pandas
  - joblib
  - sklearn2pmml
- R (optional)
  - pmml
  - e1071
  
## Instructions

- Place unzipped Ragnarock maps in `data/yourfoldername`.
- Open `TrainModel.ipynb` with Jupyter notebook.
- Change the constant `MAP_FOLDER` in the second cell to `data/yourfoldername`.  
- A `.pmml` file will be exported to the root directory. 
- For R export:
  - Make sure `data/features.csv` is present.
  - Run `TrainModel.R` using R. 
  - A different `.pmml` file will be exported to the root directory.


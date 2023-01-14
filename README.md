# Edda-MLDP

A difficulty rank predictor for Ragnarock maps powered by machine learning.

## Requirements

- Python 3
  - numpy
  - pandas
  - joblib
  - scikit-learn
  - sklearn2pmml
- R (optional)
  - pmml
  - e1071
  
## Instructions

### Model Training

- Place unzipped Ragnarock maps in `data/yourfoldername`.
- Open `TrainModel.ipynb` with Jupyter notebook.
- Change the constant `MAP_FOLDER` in the second cell to `data/yourfoldername`.  
- A `.pmml` file will be exported to the root directory. 
- For R export:
  - Make sure `data/features.csv` is present.
  - Run `TrainModel.R` using R. 
  - A different `.pmml` file will be exported to the root directory.

### Model Execution

Make sure you have the required Python packages installed, and download the `.joblib` model from the releases section.  

#### From Python

```py
import RunModel

predictions = RunModel.predictDifficulty("path/to/Edda-MLDP-Python.joblib", "path/to/my/map")

for result in predictions:
    print(result)
```

#### From terminal

```sh
$ python RunModel.py Edda-MLDP-Python.joblib path/to/my/map
```

The program will print its predictions to stdout. 

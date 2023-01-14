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

### Running the model

Make sure you have the required Python packages installed, and download the `.joblib` model from the [releases](https://github.com/PKBeam/Edda-MLDifficultyPredictor/releases) section.  

You can either run the model from a terminal for quick results, or import the Python file for use in your code project.

#### From terminal

```sh
python RunModel.py Edda-MLDP-Python.joblib path/to/my/map
```

The program will print its predictions to stdout. 

#### From Python

```py
import RunModel

predictions = RunModel.predictDifficulty("path/to/Edda-MLDP-Python.joblib", "path/to/my/map")

for result in predictions:
    print(result)
```

### Training the model

- Place unzipped Ragnarock maps in `data/yourfoldername`.
- Open `TrainModel.ipynb` with Jupyter notebook.
- Change the constant `MAP_FOLDER` in the second cell to `data/yourfoldername`.  
- A `.pmml` file will be exported to the root directory. 
- For R export:
  - Copy the training dataset `.csv` to `data/features.csv`.
  - Run `TrainModel.R` using R. 
  - A different `.pmml` file will be exported to the root directory.

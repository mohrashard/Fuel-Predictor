# Vehicle Fuel Consumption & Emissions Predictor

A machine learning project that predicts vehicle fuel consumption and CO2 emissions based on vehicle specifications using Random Forest regression.

## 📊 Overview

This project uses historical vehicle data from 2000-2022 to train a machine learning model that can predict:
- **Fuel Consumption** (L/100km)
- **CO2 Emissions** (g/km)

The model takes vehicle specifications as input and provides accurate predictions for fuel efficiency and environmental impact.

## 🗂️ Project Structure

```
MACHINE-LEARNING/
└── Fuel-Predictor/
    ├── .venv/                          # Virtual environment
    ├── model/
    │   └── vehicle_consumption_emissions_model.joblib  # Trained model (not included - too large)
    ├── Fuel_Consumption_2000-2022.csv  # Dataset
    ├── ml.ipynb                        # Jupyter notebook
    ├── model.py                        # Model training script
    └── README.md                       # This file
```

## 🚀 Features

### Input Features
- **MAKE**: Vehicle manufacturer (Toyota, Honda, BMW, etc.)
- **MODEL**: Specific vehicle model
- **VEHICLE CLASS**: Type of vehicle (Compact, SUV, Mid-size, etc.)
- **ENGINE SIZE**: Engine displacement in liters
- **CYLINDERS**: Number of engine cylinders
- **TRANSMISSION**: Transmission type (Automatic, Manual, etc.)
- **FUEL**: Fuel type (Regular gasoline, Premium, Diesel, etc.)

### Output Predictions
- **Fuel Consumption**: Combined fuel consumption in L/100km
- **CO2 Emissions**: Carbon dioxide emissions in g/km

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip or conda package manager

### Required Packages
```bash
# Using pip
pip install joblib pandas numpy scikit-learn matplotlib seaborn

# Using conda
conda install -c conda-forge joblib pandas numpy scikit-learn matplotlib seaborn
```

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Install required dependencies (the script will check and prompt if packages are missing)
4. Ensure you have the dataset file `Fuel_Consumption_2000-2022.csv` in the project root

## 📈 Usage

### Training the Model
Run the model training script to create a new model:

```bash
python model.py
```

This will:
- Load and preprocess the dataset
- Train a Random Forest model
- Evaluate model performance
- Display feature importance analysis
- Save the trained model to `model/vehicle_consumption_emissions_model.joblib`

### Making Predictions
Run the prediction interface:

```bash
python ml.ipynb
```

The interactive interface will guide you through:
1. Selecting vehicle manufacturer from 39 available makes
2. Entering vehicle model
3. Choosing vehicle class
4. Specifying engine specifications
5. Selecting transmission and fuel type

### Example Prediction
```python
# Example vehicle specifications
vehicle_specs = {
    'MAKE': 'TOYOTA',
    'MODEL': 'COROLLA',
    'VEHICLE CLASS': 'COMPACT',
    'ENGINE SIZE': 1.8,
    'CYLINDERS': 4,
    'TRANSMISSION': 'AS',  # Automatic with Select Shift
    'FUEL': 'X'           # Regular Gasoline
}

# Expected output:
# Fuel Consumption: ~7.2 L/100km
# CO2 Emissions: ~168 g/km
```

## 🎯 Model Performance

The Random Forest model achieves:
- **High R² scores** for both fuel consumption and emissions prediction
- **Low RMSE values** indicating accurate predictions
- **Feature importance analysis** showing engine size and vehicle class as top predictors

### Supported Vehicle Makes
Acura, Alfa Romeo, Aston Martin, Audi, Bentley, BMW, Buick, Cadillac, Chevrolet, Chrysler, Dodge, Fiat, Ford, Genesis, GMC, Honda, Hyundai, Infiniti, Jaguar, Jeep, Kia, Lamborghini, Land Rover, Lexus, Lincoln, Maserati, Mazda, Mercedes-Benz, Mini, Mitsubishi, Nissan, Porsche, Ram, Rolls-Royce, Subaru, Tesla, Toyota, Volkswagen, Volvo

### Vehicle Classes
Compact, SUV, Mid-size, Full-size, Two-seater, Minicompact, Subcompact, Pickup Truck, Minivan, Station Wagon, Van

### Transmission Types
- **A**: Automatic
- **AM**: Automated Manual
- **AS**: Automatic with Select Shift
- **AV**: Continuously Variable
- **M**: Manual

### Fuel Types
- **X**: Regular Gasoline
- **Z**: Premium Gasoline
- **D**: Diesel
- **E**: Ethanol (E85)
- **N**: Natural Gas

## 📊 Data Analysis Features

The training script provides comprehensive analysis:
- Data preprocessing and cleaning
- Missing value handling
- Feature importance visualization
- Model performance metrics
- Prediction vs actual value plots

## ⚠️ Important Notes

### Model File Not Included
The trained model file (`vehicle_consumption_emissions_model.joblib`) is **not included** in this repository due to its large size. You need to:
1. Run `python model.py` to train and generate the model file
2. Ensure you have the dataset `Fuel_Consumption_2000-2022.csv`
3. The model will be saved automatically after training

### 📊 Dataset Requirements

- The dataset must include vehicle fuel consumption and emissions data from the years **2000 to 2022**.
- 📁 **Dataset Source:** [Fuel Consumption Dataset on Kaggle](https://www.kaggle.com/datasets/ahmettyilmazz/fuel-consumption)


## 🔧 Troubleshooting

### Common Issues
1. **Missing packages**: The script will automatically detect and prompt for installation
2. **Model file not found**: Run the training script first to generate the model
3. **Dataset not found**: Ensure `Fuel_Consumption_2000-2022.csv` is in the project root
4. **Memory issues**: The Random Forest model requires sufficient RAM for training

### Performance Tips
- The model performs best with complete vehicle specifications
- Fuel efficiency ratings are contextualized (excellent < 6 L/100km, poor > 12 L/100km)
- For unknown vehicle models, the system will still provide predictions based on other specifications

## 📝 License

This project is for educational and research purposes. Please ensure proper attribution when using the code or methodology.

## 🤝 Contributing

Feel free to contribute by:
- Improving model accuracy
- Adding more vehicle specifications
- Enhancing the user interface
- Optimizing performance
- Adding visualization features

## 📞 Support

If you encounter issues:
1. Check that all dependencies are installed
2. Verify the dataset file is present
3. Ensure you've run the training script to generate the model
4. Check Python version compatibility (3.7+)

import os
import sys

# Check for required dependencies and install if necessary
required_packages = ['joblib', 'pandas', 'numpy', 'sklearn']
missing_packages = []

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        missing_packages.append(package)

if missing_packages:
    print(f"Missing required packages: {', '.join(missing_packages)}")
    print("\nYou need to install the missing packages. Please run the following command:")
    print(f"\nconda install -c conda-forge {' '.join(missing_packages)}")
    print("\nor")
    print(f"\npip install {' '.join(missing_packages)}")
    print("\nAfter installing the packages, run this script again.")
    sys.exit(1)

# Now import the required packages
import joblib
import pandas as pd
import numpy as np


def load_model(model_path='Fuel-Predictor/model/vehicle_consumption_emissions_model.joblib'):
    """
    Load the trained model from disk.
    
    Args:
        model_path: Path to the saved model file
        
    Returns:
        Loaded model pipeline
    """
    try:
        print(f"Loading model from {model_path}...")
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def predict_vehicle_consumption_emissions(model, vehicle_specs):
    """
    Predict fuel consumption and CO2 emissions for a vehicle.
    
    Args:
        model: Trained model pipeline
        vehicle_specs: Dictionary with vehicle specifications
            (MAKE, MODEL, VEHICLE CLASS, ENGINE SIZE, CYLINDERS, TRANSMISSION, FUEL)
    
    Returns:
        Dictionary with predicted fuel consumption and CO2 emissions
    """
    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame([vehicle_specs])
    
    # Make predictions
    predictions = model.predict(input_df)
    
    # Return results
    return {
        'Fuel Consumption (COMB L/100km)': predictions[0][0],
        'CO2 Emissions (g/km)': predictions[0][1]
    }


def get_user_input():
    """
    Get vehicle specifications from user input.
    
    Returns:
        Dictionary with vehicle specifications
    """
    print("\nPlease enter the following vehicle specifications:")
    
    makes = ["ACURA", "ALFA ROMEO", "ASTON MARTIN", "AUDI", "BENTLEY", "BMW", "BUICK", 
             "CADILLAC", "CHEVROLET", "CHRYSLER", "DODGE", "FIAT", "FORD", "GENESIS", 
             "GMC", "HONDA", "HYUNDAI", "INFINITI", "JAGUAR", "JEEP", "KIA", "LAMBORGHINI", 
             "LAND ROVER", "LEXUS", "LINCOLN", "MASERATI", "MAZDA", "MERCEDES-BENZ", 
             "MINI", "MITSUBISHI", "NISSAN", "PORSCHE", "RAM", "ROLLS-ROYCE", "SUBARU", 
             "TESLA", "TOYOTA", "VOLKSWAGEN", "VOLVO"]
    
    vehicle_classes = ["COMPACT", "SUV", "MID-SIZE", "FULL-SIZE", "TWO-SEATER", 
                       "MINICOMPACT", "SUBCOMPACT", "PICKUP TRUCK", "MINIVAN", 
                       "STATION WAGON", "VAN"]
    
    transmission_types = ["A", "AM", "AS", "AV", "M"]
    
    fuel_types = ["X", "Z", "D", "E", "N"]
    
    # Print make options with numbers
    print("\nAvailable Makes:")
    for i, make in enumerate(makes, 1):
        print(f"{i}. {make}", end="\t")
        if i % 4 == 0:
            print()
    
    make_index = int(input("\nEnter the number for MAKE: ")) - 1
    make = makes[make_index] if 0 <= make_index < len(makes) else "TOYOTA"
    
    model = input("Enter MODEL (e.g., COROLLA): ").upper()
    
    # Print vehicle class options with numbers
    print("\nAvailable Vehicle Classes:")
    for i, vc in enumerate(vehicle_classes, 1):
        print(f"{i}. {vc}", end="\t")
        if i % 3 == 0:
            print()
    
    vc_index = int(input("\nEnter the number for VEHICLE CLASS: ")) - 1
    vehicle_class = vehicle_classes[vc_index] if 0 <= vc_index < len(vehicle_classes) else "COMPACT"
    
    engine_size = float(input("Enter ENGINE SIZE in liters (e.g., 1.8): "))
    cylinders = int(input("Enter number of CYLINDERS (e.g., 4): "))
    
    # Print transmission types with explanation
    print("\nAvailable Transmission Types:")
    print("1. A  - Automatic")
    print("2. AM - Automated Manual")
    print("3. AS - Automatic with Select Shift")
    print("4. AV - Continuously Variable")
    print("5. M  - Manual")
    
    trans_index = int(input("Enter the number for TRANSMISSION: ")) - 1
    transmission = transmission_types[trans_index] if 0 <= trans_index < len(transmission_types) else "AS"
    
    # Print fuel types with explanation
    print("\nAvailable Fuel Types:")
    print("1. X - Regular Gasoline")
    print("2. Z - Premium Gasoline")
    print("3. D - Diesel")
    print("4. E - Ethanol (E85)")
    print("5. N - Natural Gas")
    
    fuel_index = int(input("Enter the number for FUEL: ")) - 1
    fuel = fuel_types[fuel_index] if 0 <= fuel_index < len(fuel_types) else "X"
    
    return {
        'MAKE': make,
        'MODEL': model,
        'VEHICLE CLASS': vehicle_class,
        'ENGINE SIZE': engine_size,
        'CYLINDERS': cylinders,
        'TRANSMISSION': transmission,
        'FUEL': fuel
    }


def display_results(vehicle_specs, predictions):
    """
    Display the vehicle specifications and predictions.
    
    Args:
        vehicle_specs: Dictionary with vehicle specifications
        predictions: Dictionary with predictions
    """
    # Transmission type mapping for display
    transmission_mapping = {
        'A': 'Automatic',
        'AM': 'Automated Manual',
        'AS': 'Automatic with Select Shift',
        'AV': 'Continuously Variable',
        'M': 'Manual'
    }
    
    # Fuel type mapping for display
    fuel_mapping = {
        'X': 'Regular Gasoline',
        'Z': 'Premium Gasoline',
        'D': 'Diesel',
        'E': 'Ethanol (E85)',
        'N': 'Natural Gas'
    }
    
    print("\n" + "="*50)
    print(" "*15 + "VEHICLE SPECIFICATIONS")
    print("="*50)
    print(f"Make: {vehicle_specs['MAKE']}")
    print(f"Model: {vehicle_specs['MODEL']}")
    print(f"Vehicle Class: {vehicle_specs['VEHICLE CLASS']}")
    print(f"Engine Size: {vehicle_specs['ENGINE SIZE']} L")
    print(f"Cylinders: {vehicle_specs['CYLINDERS']}")
    print(f"Transmission: {transmission_mapping.get(vehicle_specs['TRANSMISSION'], vehicle_specs['TRANSMISSION'])}")
    print(f"Fuel Type: {fuel_mapping.get(vehicle_specs['FUEL'], vehicle_specs['FUEL'])}")
    
    print("\n" + "="*50)
    print(" "*20 + "PREDICTIONS")
    print("="*50)
    print(f"Fuel Consumption: {predictions['Fuel Consumption (COMB L/100km)']:.2f} L/100km")
    print(f"CO2 Emissions: {predictions['CO2 Emissions (g/km)']:.2f} g/km")
    
    # Add some context to the results
    if predictions['Fuel Consumption (COMB L/100km)'] < 6:
        efficiency = "excellent (very efficient)"
    elif predictions['Fuel Consumption (COMB L/100km)'] < 8:
        efficiency = "good (efficient)"
    elif predictions['Fuel Consumption (COMB L/100km)'] < 10:
        efficiency = "average"
    elif predictions['Fuel Consumption (COMB L/100km)'] < 12:
        efficiency = "below average (inefficient)"
    else:
        efficiency = "poor (very inefficient)"
    
    print(f"\nThis vehicle's fuel efficiency is {efficiency}.")
    print("="*50)


def main():
    """Main function to run the model."""
    print("=" * 70)
    print(" " * 15 + "VEHICLE FUEL CONSUMPTION & EMISSIONS PREDICTOR")
    print("=" * 70)
    
    # Load trained model
    model = load_model()
    
    if model is None:
        print("\nCould not load the model. Please ensure the model file exists.")
        return
    
    while True:
        # Get user input
        vehicle_specs = get_user_input()
        
        # Make predictions
        predictions = predict_vehicle_consumption_emissions(model, vehicle_specs)
        
        # Display results
        display_results(vehicle_specs, predictions)
        
        # Ask if user wants to try another vehicle
        another = input("\nWould you like to try another vehicle? (y/n): ").lower()
        if another != 'y':
            break
    
    print("\nThank you for using the Vehicle Fuel Consumption & Emissions Predictor!")


if __name__ == "__main__":
    main()
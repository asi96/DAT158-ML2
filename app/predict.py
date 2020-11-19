import numpy as np
import pandas as pd
import joblib

####### 
## Get the model trained in the notebook 
# `../nbs/1.0-asl-train_model.ipynb`
#######

model = joblib.load('models/price_house_model.joblib')
pipeline = joblib.load('models/pipeline.joblib')


def preprocess(data):
    """
    Returns the features entered by the user in the web form. 

    To simplify, we set a bunch of default values. 
            For bools and ints, use the most frequent value
            For floats, use the median value

    Note that this represent some major assumptions that you'd 
    not want to make in real life. If you want to use default 
    values for some features then you'll have to think more 
    carefully about what they should be. 

    F.ex. if the user doesn't provide a value for BMI, 
    then one could use a value that makes more sense than 
    below. For example, the mean for the given gender would 
    at least be a bit more correct. 
    
    Having _dynamic defaults_ is important. And of course, if 
    relevant, getting some of the features without asking the user. 
    E.g. if the user is logged in and you can pull information 
    form a user profile. Or if you can compute or obtain the information 
    thorugh other means (e.g. user location if shared etc).
    """


    feature_values = {
        
        'MSSubClass': 90,
        'MSZoning': "RL",
        'LotFrontage': 70,
        'LotArea': 10500,
        'Street': "Pave",
        'LotShape': "Reg",
        'LandContour': "Lvl",
        'Utilities': "AllPub",
        'LotConfig': "Inside",
        'LandSlope': "Gtl",
        'Neighborhood': "MeadowV",
        'Condition1': "Norm",
        'Condition2': "Norm",
        'BldgType': "1Fam",
        'HouseStyle': "1Story",
        'OverallQual': 5,
        'OverallCond': 5,
        'YearBuilt': 1971,
        'YearRemodAdd': 1984,
        'RoofStyle': "Gable",
        'RoofMatl': "ClyTile",
        'Exterior1st': "Plywood",
        'Exterior2nd': "Stone",
        'MasVnrType': "None",
        'MasVnrArea': 103,
        'ExterQual': "TA",
        'ExterCond': "TA",
        'Foundation': "PConc",
        'BsmtQual': "TA",
        'BsmtCond': "TA",
        'BsmtExposure': "Av",
        'BsmtFinType1': "ALQ",
        'BsmtFinSF1': 443,
        'BsmtFinType2': "ALQ",
        'BsmtFinSF2': 46,
        'BsmtUnfSF': 567,
        'TotalBsmtSF': 1057,
        'Heating': "Floor",
        'HeatingQC': "TA",
        'CentralAir': "N",
        'Electrical': "FuseA",
        '1stFlrSF': 1162,
        '2ndFlrSF': 346,
        'LowQualFinSF': 5,
        'GrLivArea': 1515,
        'BsmtFullBath': 0,
        'BsmtHalfBath': 0,
        'FullBath': 0,
        'HalfBath': 0,
        'BedroomAbvGr': 2,
        'KitchenAbvGr': 1,
        'KitchenQual': "TA",
        'TotRmsAbvGrd': 6,
        'Functional': "Typ",
        'Fireplaces': 0,
        'FireplaceQu': "TA",
        'GarageType': "Basement",
        'GarageYrBlt': 1978,
        'GarageFinish': "Fin",
        'GarageCars': 1,
        'GarageArea': 472,
        'GarageQual': "TA",
        'GarageCond': "TA",
        'PavedDrive': "P",
        'WoodDeckSF': 94,
        'OpenPorchSF': 46,
        'EnclosedPorch': 21,
        '3SsnPorch': 3,
        'ScreenPorch': 15,
        'PoolArea': 2,
        'MiscVal': 43,
        'MoSold': 6,
        'YrSold': 2007,
        'SaleType': "New",
        'SaleCondition': "Normal"
    }


    # Parse the form inputs and return the defaults updated with values entered.

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values



####### 
## Now we can predict with the trained model:
#######


def predict(data):
    """
    If debug, print various useful info to the terminal.
    """
 
    # Store the data in an array in the correct order:

    column_order = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'LotShape',
       'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
       'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt',
       'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd',
       'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation',
       'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 
       'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
       'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd',
       'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt',
       'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond',
       'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
       'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
       'SaleCondition']

    data = np.array([data[feature] for feature in column_order], dtype=object)
    

    # NB: In this case we didn't do any preprocessing of the data before 
    # training our random forest model (see the notebool `nbs/1.0-asl-train_model.ipynb`). 
    # If you plan to feed the training data through a preprocessing pipeline in your 
    # own work, make sure you do the same to the data entered by the user before 
    # predicting with the trained model. This can be achieved by saving an entire 
    # sckikit-learn pipeline, for example using joblib as in the notebook.
    preparedData = pipeline.transform(data.reshape(1,-1))
    
    pred = model.predict(preparedData.reshape)

    uncertainty = model.predict_proba(preparedData)

    return pred, uncertainty


def postprocess(prediction):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc. 
    """

    pred, uncertainty = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try: 
        int(pred[0]) > 0
    except:
        pass

    # Make strings
    pred = str(pred[0])
    uncertainty = str(uncertainty[0])


    # Return
    return_dict = {'pred': pred, 'uncertainty': uncertainty}

    return return_dict
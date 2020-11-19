from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values for house price prediction. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    # Selected features with the highest impact - can uncomment more if interested
    MSSubClass = IntegerField('MSSubClass: Type of dwelling involved in the sale', validators=[NumberRange(min=20, max=190)])
    MSZoning = StringField('MSZoning: The general zoning classification of the sale')
    LotFrontage = FloatField('LotFrontage: Linear feet of street connected to property')
    LotArea = IntegerField('LotArea: Lot size in square feet')
    '''
    Street = StringField('Street: Type of road access to property')
    LotShape = StringField('LotShape: General shape of property')
    LandContour = StringField('LotShape: General shape of property')
    Utilities = StringField('Utilities: Type of utilities available')
    LotConfig = StringField('LotConfig: Lot configuration')
    LandSlope = StringField('LandSlope: Slope of property')
    Neighborhood = StringField('Neighborhood: Physical locations within Ames city limits')
    Condition1 = StringField('Condition1: Proximity to various conditions')
    Condition2 = StringField('Condition2: Proximity to various conditions (if more than one is present')
    BldgType = StringField('BldgType: Type of dwelling')
    HouseStyle = StringField('HouseStyle: Style of dwelling')
    '''
    OverallQual = IntegerField('OverallQual: Rates the overall material and finish of the house', validators=[NumberRange(min=1, max=10)])
    OverallCond = IntegerField('OverallCond: Rates the overall condition of the house', validators=[NumberRange(min=1, max=10)])
    YearBuilt = IntegerField('YearBuilt: Original construction date')
    YearRemodAdd = IntegerField('Remodel date (same as construction date if no remodeling or additions)')
    '''
    RoofStyle = StringField('RoofStyle: Type of roof')
    RoofMatl = StringField('RoofMatl: Roof material')
    Exterior1st = StringField('Exterior1st: Exterior covering on house')
    Exterior2nd = StringField('Exterior2nd: Exterior covering on house (if more than one material)')
    MasVnrType = StringField('MasVnrType: Masonry veneer type')
    MasVnrArea = FloatField('MasVnrArea: Masonry veneer area in square feet')
    ExterQual = StringField('ExterQual: Evaluates the quality of the material on the exterior')
    ExterCond = StringField('ExterCond: Evaluates the present condition of the material on the exterior')
    Foundation = StringField('Foundation: Type of foundation')
    BsmtQual = StringField('BsmtQual: Evaluates the height of the basement')
    BsmtCond = StringField('BsmtCond: Evaluates the general condition of the basement')
    BsmtExposure = StringField('BsmtExposure: Refers to walkout or garden level walls')
    BsmtFinType1 = StringField('BsmtFinType1: Rating of basement finished area')
    BsmtFinSF1 = IntegerField('BsmtFinSF1: Type 1 finished square feet')
    BsmtFinType2 = StringField('BsmtFinType2: Rating of basement finished area (if multiple types)')
    BsmtFinSF2 = IntegerField('BsmtFinSF2: Type 2 finished square feet')
    BsmtUnfSF = IntegerField('BsmtUnfSF: Unfinished square feet of basement area')
    TotalBsmtSF = IntegerField('TotalBsmtSF: Total square feet of basement area')
    Heating = StringField('Heating: Type of heating')
    HeatingQC = StringField('HeatingQC: Heating quality and condition')
    CentralAir = StringField('CentralAir: Central air conditioning')
    Electrical = StringField('Electrical: Electrical system')
    ## Python disallows variables starting with a number
    ##1stFloorSF = IntegerField('1stFlrSF: First Floor square feet')
    ##2ndFloorSF = IntegerField('2ndFlrSF: Second floor square feet')
    LowQualFinSF = IntegerField('LowQualFinSF: Low quality finished square feet (all floors)')
    '''
    GrLivArea = IntegerField('GrLivArea: Above grade (ground) living area square feet')
    BsmtFullBath = IntegerField('BsmtFullBath: Basement full bathrooms')
    BsmtHalfBath = IntegerField('BsmtHalfBath: Basement half bathrooms')
    FullBath = IntegerField('FullBath: Full bathrooms above grade')
    '''
    HalfBath = IntegerField('HalfBath: Half baths above grade')
    BedroomAbvGr = IntegerField('BedroomAbvGr: Bedrooms above grade (does NOT include basement bedrooms)')
    KitchenAbvGr = IntegerField('KitchenAbvGr: Kitchens above grade')
    KitchenQual = StringField('KitchenQual: Kitchen quality')
    TotRmsAbvGrd = IntegerField('TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)')
    Functional = StringField('Functional: Home functionality (Assume typical unless deductions are warranted)')
    Fireplaces = IntegerField('Fireplaces: Number of fireplaces')
    FireplaceQu = StringField('FireplaceQu: Fireplace quality')
    GarageType = StringField('GarageType: Garage location')
    GarageYrBlt = FloatField('GarageYrBlt: Year garage was built')
    GarageFinish = StringField('GarageFinish: Interior finish of the garage')
    '''
    GarageCars = IntegerField('GarageCars: Size of garage in car capacity')
    GarageArea = IntegerField('GarageArea: Size of garage in square feet')
    '''
    GarageQual = StringField('GarageQual: Garage quality')
    GarageCond = StringField('GarageCond: Garage condition')
    PavedDrive = StringField('PavedDrive: Paved driveway')
    WoodDeckSF = IntegerField('WoodDeckSF: Wood deck area in square feet')
    OpenPorchSF = IntegerField('OpenPorchSF: Open porch area in square feet')
    EnclosedPorch = IntegerField('EnclosedPorch: Enclosed porch area in square feet')
    ## Python disallows variables starting with a number
    ##ThreeSsnPorch = IntegerField('3SsnPorch: Three season porch area in square feet')
    ScreenPorch = IntegerField('ScreenPorch: Screen porch area in square feet')
    PoolArea = IntegerField('PoolArea: Pool area in square feet')
    MiscVal = IntegerField('MiscVal: $Value of miscellaneous feature')
    MoSold = IntegerField('MoSold: Month Sold (MM)', validators=[NumberRange(min=1, max=12)])
    YrSold = IntegerField('YrSold: Year Sold (YYYY)')
    SaleType = StringField('SaleType: Type of sale')
    SaleCondition = StringField('SaleCondition: Condition of sale')
    '''
    submit = SubmitField('Submit')


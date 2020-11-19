# Machine Learning - House Price Prediction in Ames, Iowa
![Alt text](assets/housesbanner.png?raw=true "Houses")
This is my hand in to machine learning project 2 in the course DAT158 as well as my submission to the Kaggle contest https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview


The machine learning model has been deployed and can be run locally by executing the following command in a python terminal:

`python housepriceapp.py`

There are currently some categorical data not recognized by the machine learning model so if a category value produces an
error try another until it works. This is a result of a small initial dataset not having every category represented
which was fitted into the prediction model.

Features not show in the demo form has default/median values assigned to them.

If you want more features available you can uncomment them in `features.py` located in `app/forms.py`.

Demo preview:
![Alt text](assets/demo.png?raw=true "Houses")

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/h571740/DAT158-ML2/HEAD?filepath=notebooks%2FML%20Nr%202%20-%20Playing%20the%20Whole%20Game.ipynb)

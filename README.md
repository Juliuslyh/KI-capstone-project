# KI-capstone-project
## Usage
1.Date file stores all the collected used for modeling.

2.DataCollection file contains all scripts for crawling data. 

run GenerateData.py to crawl beer sales data, review data, holiday data, and weather data. (It takes hours to crawl all the data from different websites.)  Use command 'pip install -r requirements.txt' to install related libraries.

use Google Colab to run the scripts in GDELT and Twitter file

3.FeatureEngineering _ Modeling file contains two scripts:

Classification_model.ipynb(run with Google Colab) is used for building the classification models, which are text classification and sentiment analysis.

FeatureEngineering_for_RegressionModel.ipynb(run with Jupyter notebook) is used for building the regression model to forecast beer sales. 

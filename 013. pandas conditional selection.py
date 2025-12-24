import pandas as pd

ml_models_data=pd.read_csv("./python-simple-programs/013. nn_models_data.csv")
ml_models_data=ml_models_data.set_index("Model_Name")
print (ml_models_data)
#do the conditional selection next


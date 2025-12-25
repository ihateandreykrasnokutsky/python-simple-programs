import pandas as pd

ml_models_data=pd.read_csv("./python-simple-programs/013. nn_models_data.csv")
ml_models_data=ml_models_data.set_index("Model_Name")
print (ml_models_data)
#do the conditional selection next
#developer selection
developer_needed="Stability AI"
ml_models_data_developer=ml_models_data.Developer==developer_needed
print ("CONDITIONAL SELECTION FOR", developer_needed, "DEVELOPER")
print (ml_models_data_developer)
#parameter count selection
pc_threshold=1000
ml_models_data_pc=ml_models_data.Parameter_Count_M>pc_threshold
print (("CONDITIONAL SELECTION FOR", pc_threshold, "M PARAMETER COUNT"))
result=pd.concat([ml_models_data_pc, ml_models_data.Parameter_Count_M], axis=1) #combine data frames with parameter count and true/false.
print (result)
#done with condsitional selection



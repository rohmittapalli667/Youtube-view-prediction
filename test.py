import pickle
with open('RandomForest_model.pkl','rb') as file:
    object = pickle.load(file)

print(object)
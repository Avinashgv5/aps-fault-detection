import pymongo
import pandas as pd
import json

# provide mongodb to connect local host url by python
client=pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns:  {df.shape}")
    #convert data frame to json so that we can dump these record in mongodb
    df.reset_index(drop=True,inplace=True)

    json_record= list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


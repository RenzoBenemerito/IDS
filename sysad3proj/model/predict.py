import pandas as pd
import io
import requests
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn import metrics
from keras.models import Sequential, load_model
#create_model, set_weights, compile, compile_params
from keras.layers.core import Dense, Activation
from keras.callbacks import EarlyStopping, ModelCheckpoint
import functions as f
class prediction():
    def extract(self,packet):
        return packet

    def addCol(self,df):
        df.columns = [
        'duration',
        'protocol_type',
        'service',
        'flag',
        'src_bytes',
        'dst_bytes',
        'land',
        'wrong_fragment',
        'urgent',
        'hot',
        'num_failed_logins',
        'logged_in',
        'num_compromised',
        'root_shell',
        'su_attempted',
        'num_root',
        'num_file_creations',
        'num_shells',
        'num_access_files',
        'num_outbound_cmds',
        'is_host_login',
        'is_guest_login',
        'count',
        'srv_count',
        'serror_rate',
        'srv_serror_rate',
        'rerror_rate',
        'srv_rerror_rate',
        'same_srv_rate',
        'diff_srv_rate',
        'srv_diff_host_rate',
        'dst_host_count',
        'dst_host_srv_count',
        'dst_host_same_srv_rate',
        'dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate',
        'dst_host_serror_rate',
        'dst_host_srv_serror_rate',
        'dst_host_rerror_rate',
        'dst_host_srv_rerror_rate',
        'outcome'
        ]
        return df


    def encode(self,df):
        f.encode_numeric_zscore(df, 'duration')
        f.encode_text_dummy(df, 'protocol_type')
        f.encode_text_dummy(df, 'service')
        f.encode_text_dummy(df, 'flag')
        f.encode_numeric_zscore(df, 'src_bytes')
        f.encode_numeric_zscore(df, 'dst_bytes')
        f.encode_text_dummy(df, 'land')
        f.encode_numeric_zscore(df, 'wrong_fragment')
        f.encode_numeric_zscore(df, 'urgent')
        f.encode_numeric_zscore(df, 'hot')
        f.encode_numeric_zscore(df, 'num_failed_logins')
        f.encode_text_dummy(df, 'logged_in')
        f.encode_numeric_zscore(df, 'num_compromised')
        f.encode_numeric_zscore(df, 'root_shell')
        f.encode_numeric_zscore(df, 'su_attempted')
        f.encode_numeric_zscore(df, 'num_root')
        f.encode_numeric_zscore(df, 'num_file_creations')
        f.encode_numeric_zscore(df, 'num_shells')
        f.encode_numeric_zscore(df, 'num_access_files')
        f.encode_numeric_zscore(df, 'num_outbound_cmds')
        f.encode_text_dummy(df, 'is_host_login')
        f.encode_text_dummy(df, 'is_guest_login')
        f.encode_numeric_zscore(df, 'count')
        f.encode_numeric_zscore(df, 'srv_count')
        f.encode_numeric_zscore(df, 'serror_rate')
        f.encode_numeric_zscore(df, 'srv_serror_rate')
        f.encode_numeric_zscore(df, 'rerror_rate')
        f.encode_numeric_zscore(df, 'srv_rerror_rate')
        f.encode_numeric_zscore(df, 'same_srv_rate')
        f.encode_numeric_zscore(df, 'diff_srv_rate')
        f.encode_numeric_zscore(df, 'srv_diff_host_rate')
        f.encode_numeric_zscore(df, 'dst_host_count')
        f.encode_numeric_zscore(df, 'dst_host_srv_count')
        f.encode_numeric_zscore(df, 'dst_host_same_srv_rate')
        f.encode_numeric_zscore(df, 'dst_host_diff_srv_rate')
        f.encode_numeric_zscore(df, 'dst_host_same_src_port_rate')
        f.encode_numeric_zscore(df, 'dst_host_srv_diff_host_rate')
        f.encode_numeric_zscore(df, 'dst_host_serror_rate')
        f.encode_numeric_zscore(df, 'dst_host_srv_serror_rate')
        f.encode_numeric_zscore(df, 'dst_host_rerror_rate')
        f.encode_numeric_zscore(df, 'dst_host_srv_rerror_rate')
        outcomes = f.encode_text_index(df, 'outcome')
        num_classes = len(outcomes)
        df.dropna(inplace=True,axis=1)
    
        return df

    def to_xy(self, df, target):
        df = f.to_xy(df,target)
        return df

    def predictOut(self, x_test):
        model = load_model("ids.h5")
        pred = model.predict(x_test)
        pred = np.argmax(pred,axis=1)
        outcomes = f.decode_text_index(pred)
        y_eval = np.argmax(y_test,axis=1)
        score = metrics.accuracy_score(y_eval, pred)
        print(outcomes)
        print("Validation score: {}".format(score))
        return outcomes
    
    # def main(self,):
    #     df = self.extract("haha")
    #     df = self.addCol(df)
    #     df = self.encode(df)
    #     x = self.to_xy(df, 'outcome')
    #     outcomes = self.predictOut(x)



# # print("\n\nRaw Output \n\n")
p = prediction()
df = pd.read_pickle("dfRaw.pkl")
df = p.addCol(df)
df['outcome'] = ""
#df = df.loc[df['outcome'] == 'neptune.']
print(df)

#with pd.option_context('display.max_rows', 1, 'display.max_columns', None):
#print(df.loc[df['outcome'] == 'nmap.'].values[0:5])
df = p.encode(df)
x,y = p.to_xy(df, 'outcome')

x_train, x_test, y_train, y_test = train_test_split(
     x, y, test_size=0.25, random_state=42)

p.predictOut(x)

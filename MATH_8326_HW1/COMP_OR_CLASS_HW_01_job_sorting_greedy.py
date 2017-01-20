# Becky Brusky
# Math_8326_Computation_OR
import pandas as pd
import numpy as np
import random

def days_late(df):
    # this assumes that the data frame is in order and done_date and Days_late are correct!!!!
    filter = df['days_late'] > 0
    return df[filter]['days_late'].sum()
    
def days_late(df):
    # this assumes that the data frame is in order and done_date and Days_late are correct!!!!
    filter = df['days_late'] > 0
    return df[filter]['days_late'].sum()

def recalculate_time(df):
    df['done_date'] = df.PROCESSING_TIME.cumsum()
    df['days_late'] = df['done_date'] - df['DUE_DATE']
    return df

def solver(df):
    #--------------------------------
    #     I N I T I A L    S O R T
    #--------------------------------
    # Initial Sort by PROCESSING_TIME
    df = df.sort_values(by='PROCESSING_TIME').reset_index(drop=True)
    df = recalculate_time(df)
    print('\n\nJobs sorted by PROCRESSING_TIME, Greedy Algorithm')
    print('Days late total:',days_late(df))
    print(df)


#--------------------------------
#  U s e    G i v e n    D a t a
#--------------------------------
processing_times = [33,17, 6,40,22, 8,27,19,30]
due_dates =        [35,90,43,85,60,23,76,59,99]
data = {'JOB':range(len(due_dates)),'PROCESSING_TIME':processing_times,'DUE_DATE':due_dates}
df = pd.DataFrame(data, columns = ['JOB', 'PROCESSING_TIME', 'DUE_DATE'])
df = recalculate_time(df)
print('\n\n=================  G I V E N    D A T A  =================')
print('Initial Data:')
print('Days late total:',days_late(df))
print(df)
solver(df)
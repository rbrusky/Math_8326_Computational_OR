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
    #  S P L I T    J O B S   I N T O
    #       T W O   G R O U P S
    #--------------------------------
    # Split the sorted list into two at the cummulative done_date by the last due date
    last_due_date = df.DUE_DATE.max()
    filter = df['done_date'] <= last_due_date

    #--------------------------------
    #        P H A S E   I
    #--------------------------------
    # Sort the jobs that can get done before time is up by the DUE_DATE
    # This is to maximize the number of jobs that finish on time (no penelty)
    # and minimize the over due counts
    df_A = df[filter].copy()
    df_A = df_A.sort_values(by='DUE_DATE').reset_index(drop=True)
    df_A = recalculate_time(df_A)
    print("\n\nPHASE I:   (Jobs that finish on or before day " + str(last_due_date) +')')
    print('Days late total:',days_late(df_A))
    print(df_A)

    #--------------------------------
    #        P H A S E   II
    #--------------------------------
    #Sort the jobs that will finish after the time is up by PROCESSING_TIME
    # This is to minimize the number of unfinished jobs per day after the last deadline.
    df_B = df[~filter].copy()
    df_B = df_B.sort_values(by='PROCESSING_TIME').reset_index(drop=True)
    print("\n\nPHASE II:    (Jobs that finish after " + str(last_due_date) +')')
    print(df_B)

    #--------------------------------
    #         R E S U L T S
    #--------------------------------
    df_result = pd.concat([df_A,df_B])
    df_result = recalculate_time(df_result)
    print('\n\n      R E S U L T S:   Days late total:',days_late(df_result),'\n')
    print(df_result)


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


#--------------------------------
#  U s e   R a n d o m   D a t a
#--------------------------------
for i in range(3):
    print('\n\n=================  R A N D O M    D A T A  =================')
    processing_times = []
    due_dates = []
    for i in range(12):
        x = random.choice(range(5,41))
        processing_times.append(x)
        due_dates.append(int(x * np.random.uniform(1.1, 4.6, size=1)[0]))
    data = {'JOB':range(12),'PROCESSING_TIME':processing_times,'DUE_DATE':due_dates}
    df = pd.DataFrame(data, columns = ['JOB', 'PROCESSING_TIME', 'DUE_DATE'])
    df = recalculate_time(df)
    print('Initial Data:')
    print('Days late total:', days_late(df))
    print(df)
    solver(df)
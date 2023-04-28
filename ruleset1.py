def age_check(df):
    errors = df['Age'][(df['Age']>150)|(df['Age']<0)].count()
    return errors, 'Checking if age is in range 0-150'

def age_marriage_check(df):
    errors = 0
    for i in range(len(df)):
        if df['Age'][i]<df['Yearsmarried'][i]:
            errors += 1
    return errors, 'Checking if Age is greater than Yearsmarried'

def status_check(df):
    errors = len(df) - len(df[df['Status'].isin(['single','married','widowed'])])
    return errors, 'Checking if Status is from Single, Married, or Widowed'

def agegroup_check(df):
    errors = 0
    for i in range(len(df)):
        if df['Age'][i]<18 and df['Agegroup'][i]!='child':
            errors += 1
        elif df['Age'][i]>=18 and df['Age'][i]<65 and df['Agegroup'][i]!='adult':
            errors += 1
        elif df['Age'][i]>=65 and df['Agegroup'][i]!='elderly':
            errors += 1

    return errors, 'Checking if Age Group is Violated'
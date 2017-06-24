import pandas as pd
import matplotlib.patches as mpat
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys

def year_group(year):
    yr_grp=''
    if year < 1980:
        yr_grp = 'Group 1'
    elif year < 1990:
        yr_grp = 'Group 2'
    elif year < 2000:
        yr_grp = 'Group 3'
    else: 
        yr_grp = 'Group 4'
    return yr_grp


def get_percent(df):
    new_df = df.rename(columns={'id':'total_attacks'})
    total = new_df['total_attacks'].sum()
    new_df['Percentage'] = new_df.apply(lambda x: (x['total_attacks']/total)*100, axis=1)
    return new_df


print('ucitavanje podataka...', end='')
sys.stdout.flush()
new_globalterror = pd.read_csv('datasets/backup2.csv')
new_globalterror['Group'] = new_globalterror.apply(lambda row: year_group(row['year']),axis=1)
print('gotovo')

print('izracunavanje procenata...', end='')
sys.stdout.flush()
group_1 = new_globalterror[new_globalterror.Group == 'Group 1'].groupby('weapon').count()['id'].reset_index()
group_2 = new_globalterror[new_globalterror.Group == 'Group 2'].groupby('weapon').count()['id'].reset_index()
group_3 = new_globalterror[new_globalterror.Group == 'Group 3'].groupby('weapon').count()['id'].reset_index()
group_4 = new_globalterror[new_globalterror.Group == 'Group 4'].groupby('weapon').count()['id'].reset_index()

new_grp1 = get_percent(group_1)
new_grp2 = get_percent(group_2)
new_grp3 = get_percent(group_3)
new_grp4 = get_percent(group_4)
print('gotovo')

print('cuvanje slike...', end='')
sys.stdout.flush()
plt.figure(figsize=[16,8])
sns.pointplot(x='weapon',y='Percentage', data=new_grp1[:-1], color='red')
sns.pointplot(x='weapon',y='Percentage', data=new_grp3[:-1], color='blue')
sns.pointplot(x='weapon',y='Percentage', data=new_grp2[1:],  color='green')
sns.pointplot(x='weapon',y='Percentage', data=new_grp4[1:],  color='violet')
plt.xticks(rotation=90)

plt.xlabel('Vrsta oruzja', size=16)
plt.ylabel('Zastupljenost [%]', size=16)
plt.title('Zastupljenost raslicitih vrsta oruzja', size=18)

red_l   = mpat.Patch(color='red',   label='1970-1980')
gre_l   = mpat.Patch(color='green', label='1981-1990')
blue_l  = mpat.Patch(color='blue',  label='1991-2000')
vio_l   = mpat.Patch(color='violet',label='2001-2015')
plt.legend(handles=[red_l,gre_l,blue_l,vio_l])
plt.savefig('zastupljenost-big.png', bbox_inches='tight')
print('gotovo')
sys.stdout.flush()

plt.show()


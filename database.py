import pandas as pd
import matplotlib.pyplot as plt
import xlrd

def save(location, cleaness, built_in):
    idx = len(pd.read_excel("frequency.xls"))
    new_df = pd.DataFrame({"location":location,
                           "cleaness":cleaness,
                           "built_in":built_in},
                         index = [idx])
    new_df.to_excel("frequency.xls",header=False)
    return None

def load_list():
    frequencyi = []
    df = pd.read_excel("frequency.xls")
    for i in range(len(df)):
        frequencyi.append(df.iloc[i].tolist())
        
    return frequencyi

def load_list_habit():
    habitt = []
    dfh = pd.read_excel("habit.xls")
    for i in range(len(dfh)):
        habitt.append(dfh.iloc[i].tolist())
        
    return habitt

#dfmen = df.iloc[[0]["주 3회 이상 규칙적 운동을 한다"]]
# df = pd.read_excel('./frequency.xls')
# idxl=len(pd.read_excel("frequency.xls"))
# locationl=1
# cleanessl=2
# built_inl=3
# new_dfmen = pd.DataFrame({"locationl":locationl,
#                           "cleanessl":cleanessl,
#                           "built_inl":built_inl},
#                         index = [idxl])
# new_dfmen.to_excel("frequncy.xls",mode="a",header=False)



#dfmen = df.iloc[[0]]
# print(idxl)
# print(new_dfmen)
#high_frequenc = df[df["주 3회 이상 규칙적 운동을 한다"] >= 30]

#df = pd.read_table('./report.txt', sep=',', header=None, names=['기간','대분류','분류','주 3회 이상','주 1~2회','하긴한다' ,'하지않음'])

#alive = df[df["주 3회 이상"] == 19.3]

#print(high_frequenc)



# def save(location, cleaness, built_in):
#     idx = len(pd.read_csv("database.csv"))
#     new_df = pd.DataFrame({"location":location,
#                            "cleaness":cleaness,
#                            "built_in":built_in}, 
#                          index = [idx])
#     new_df.to_csv("database.csv",mode = "a", header = False)
#     return None

# def load_list():
#     house_list = []
#     df = pd.read_csv("report.txt")
#     for i in range(len(df)):
#         house_list.append(df.iloc[i].tolist())
#     print(house_list)
#     # return house_list

# def now_index():
#     df = pd.read_csv("report.txt")
#     return len(df)-1


# def load_house(idx):
#     df = pd.read_csv("report.txt")
#     house_inf = df.iloc[idx]
#     return house_info


# if __name__ =="__main__":
#     load_list()
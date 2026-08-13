import pandas as pd

def import_file() -> pd.DataFrame:
    """
    Imports the data file into the dataframe
    
    Parameter:
    N/A
    
    Returns:
    Dataframe: raw data in Dataframe
    
    """
    
    df = pd.read_excel('MRCC.xlsx')
    return df

def find_boolean_columns(df) -> list:
    
    """
    Filters out columns that determine if Ability # has CC
    
    Parameter:
    DataFrame: Raw Data
    
    Returns:
    List: All Boolean Column Names
    
    """
    
    boolean_columns = ["Character"]
    
    for column in df.columns:
        if "(Y/N)" in column:
            boolean_columns.append(column)
    return boolean_columns
    
def num_of_cc_abilities(df, boolean_columns):
    """
    Finds how many abilities have Crowd Control for each character and adds it to the raw data
    
    Parameter:
    DataFrame: raw data
    
    """
    
    df["Number of CC Abilities"]= df[boolean_columns].apply(lambda row: (row == "Y").sum(), axis = 1) 

def char_highest_per_role(df, highest_per_role):
    """
    Subhelper method that uses the highest frequency per role to find the culprits in each role
        
    Parameter:
    DataFrame: cleaned data
    Series: highest frequency of CC abiltiies in each role
    
    Return: 
    Dictionary: K --> Role, V --> List of Characters with Highest Number of CC abilties in that Role
    
    """
    
    HPR_dict = highest_per_role.to_dict()
    #print(HPR_dict)
    res = {}
    
    for role, freq in HPR_dict.items():
        if role not in res:
            res[role] = []
            
        res[role].append(df[(df["Role"] == role) & (df["Number of CC Abilities"] == freq)]["Character"].tolist())
        
    return res
        
def update_excel_file(df):
    """
    Exports the clean data into a new excel file
    
    Parameter:
    DataFrame: clean data
    
    """
    df.to_excel("MRCC_Updated.xlsx")

def statistics(df):
    """
    Basic analysis of the data
    
    Parameter:
    DataFrame: raw data
    
    """
    num_of_chars_per_role = df.groupby("Role").size()
    mean = df.groupby("Role")["Number of CC Abilities"].mean()
    std = df.groupby("Role")["Number of CC Abilities"].std()
    sum_of_all_CC_abilities = df["Number of CC Abilities"].sum()
    highest_per_class = df.groupby("Role")["Number of CC Abilities"].max()
    char_with_highest_number_of_cc = df["Number of CC Abilities"].idxmax()
    highest_num_of_cc = df["Number of CC Abilities"].max()
     
    biggest_culprits_per_role = char_highest_per_role(df, highest_per_class)
    
    print(f"How Many Characters for Each {num_of_chars_per_role} \n" )
    print(f"The Mean of CC Abilities Across Each {mean} \n")
    print(f"The Standard Deviation of CC Abilities Across Each {std} \n")
    print("How many abilities in the game have CC total? ", sum_of_all_CC_abilities)
    print(f"\nHighest Frequency of CC Abilities From a Singular Character Across Each {highest_per_class} \n")
    
    ## note, need to fix since there are multiple characters with the highest amount of cc in their class (Vanguard and Duelist)
    for role, val in biggest_culprits_per_role.items():
        print(f"The Biggest Culprits in {role} is/are {val[0]}")
    
    print(f"\nCharacter with the most amount of CC OVERALL is {df.iloc[char_with_highest_number_of_cc]["Character"]} with {highest_num_of_cc} CC abilities\n")

def main(): 
    """
    Main Function
    
    """
    
    #import the file from the folder
    df = import_file()
    
    #find all of the columns that identify if an abilty has CC 
    boolean_columns = find_boolean_columns(df)
    
    #add a column to the raw data that counts how many CCs each character has
    num_of_cc_abilities(df, boolean_columns)
    
    statistics(df)
    
    #export the data out to a new excel file
    #update_excel_file(df)
    
    
main()
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
    
      
def num_of_cc_abilties(df, boolean_columns):
    """
    Finds how many abilities have Crowd Control for each character and adds it to the raw data
    
    Parameter:
    DataFrame: raw data
    
    """
    
    df["Number of CC Abilties"]= df[boolean_columns].apply(lambda row: (row == "Y").sum(), axis = 1)
    
    
def update_excel_file(df):
    df.to_excel("MRCC_Updated.xlsx")

def main(): 
    """
    Main Function
    
    """
    
    #import the file from the folder
    df = import_file()
    
    #find all of the columns that identify if an abilty has CC 
    boolean_columns = find_boolean_columns(df)
    
    #add a column to the raw data that counts how many CCs each character has
    num_of_cc_abilties(df, boolean_columns)
    
    #export the data out to a new excel file
    update_excel_file(df)
    
    
main()
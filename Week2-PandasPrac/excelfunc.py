import pandas as pd
import xlrd

   
class practice: 
    
    def filereader(filename):
        '''
        This method allows the user to read the excel file and coverts it to a dataframe
        '''
        df = pd.read_excel(filename)
        
        
        headers = ['brokered_by', 'status', 'price', 'bed', 'bath', 'acre_lot', 'street', 'city', 'state', 'zip_code', 'house_size', 'prev_sold_date']
        df.columns = headers
        
        return df
    
    def getDtype(df,column_head):
        '''Returns the datatype of a specific column'''
        column_arr = df[column_head]
        return column_arr
    
    def writeto(df):
        
        df.to_excel('final.xlsx',index = False)
    
    def getColumn(df,column_head):
        '''
        From the excel / dataframe , this method extracts a column and returns it
        '''
        column = df[column_head]
        return column
    
    def replaceCT(df,column_head):
        '''Replaces the null values within the column'''
        column = df[column_head]
        dtype = str(column.dtype)
        match dtype:
            case "int64":
                mean = column.mean()
                df[column_head].fillna(mean,inplace = True)
            case "float64":
                mean = column.mean().round()
                df[column_head].fillna(mean,inplace = True)
            case "object":
                mode = column.mode()
                df[column_head].fillna(mode,inplace = True)
                
        
    def replaceNull(df):
        '''
        This method, deletes all rows with null values. Which is better for the cleaning process
        '''
        headers = df.columns.tolist()
        df.dropna(subset= headers, inplace=True)
        df.reset_index(drop=True, inplace=True)
        
    def replaceAcr(df,column_head):
        '''
        Converts all values from acres to sq feet
        Only use when needed
        '''
        print(df[column_head].tail())
        df[column_head].fillna(0,inplace = True)
        df[column_head] = df[column_head]*43560
        print(df[column_head].tail())

    


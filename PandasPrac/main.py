from excelfunc import practice

   
if __name__ == "__main__":
        fileinp = input("What file would you like to read from: ")
        df = practice.filereader(fr"{fileinp}")
        print(df.head())
        headers = df.columns.tolist()
        print(headers)
        header_inp = input("Please enter which column you would like to look at and sort: ")
        
        col_dtype = practice.getDtype(df,header_inp)
        print("This column is of type {}".format(col_dtype))
        print("Replacing Null values")
        practice.replaceCT(df,header_inp)
        print("File has been cleaned")
       
        practice.writeto(df)
        
        
                
        
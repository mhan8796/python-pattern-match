import psycopg2
import Query
import Utils

filepath="TeamMapping_2.xlsx"

def main():
    teamMapping = Utils.readxlsx(filepath)
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    #content = Query.getContent(myConnection)
    Query.getMoreContentNWriteToCsv(myConnection)

    #Utils.updateStringPatternOne(content,teamMapping)
    #Utils.updateStringPatternTwo(content,teamMapping)
    #Utils.updateStringPatternThree(content,teamMapping)
    #Utils.updateStringPatternFour(content,teamMapping)
    #Utils.updateStringPatternFive(content,teamMapping)
    #Utils.updateStringPatternSix(content,teamMapping)
    #Utils.replaceCf(content)
    #Query.updateContent(myConnection, content)

    #Utils.writeCsv(content)
    #for k,v in content.items():
        #print(k,v,'\n')
    #myConnection.commit()
    myConnection.close()


if __name__== "__main__":
    main()

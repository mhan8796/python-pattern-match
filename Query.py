import csv

def getContent(conn):
    content = {}
    cur = conn.cursor()
    cur.execute( "SELECT id,reqcontent FROM searchrequest" )
    for id,reqcontent in cur.fetchall() :
        content[id]=reqcontent
    return content

def updateContent(conn, newContent):
    sql = """UPDATE searchrequest
                SET reqcontent = %s
                WHERE id = %s"""
    for k,v in newContent.items():
        cur = conn.cursor()
        cur.execute(sql, (v, str(k)))

def getMoreContentNWriteToCsv(conn):
    w = csv.writer(open('filter.csv','w'))
    w.writerow(['id','filtername','authorname','reqcontent'])
    cur = conn.cursor()
    cur.execute( "SELECT id,filtername,authorname,reqcontent FROM searchrequest" )
    for id,filtername,authorname,reqcontent in cur.fetchall() :
        w.writerow([id, filtername,authorname,reqcontent])

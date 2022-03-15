# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json
import pymysql.cursors

def queryset():
    # Use a breakpoint in the code line below to debug your script.
    conn = pymysql.connect(
        host=""
        port=3306,
        user="",  # ex) root
        password="",
        database="",
        charset = 'utf8'
    );
    curs = conn.cursor()

    with open('bank.json') as json_file:
        json_data = json.load(json_file)

        bnkLst = json_data['resbody']['bnkLst']

        for i in bnkLst:
            bnkNm = i['bnkNm']
            bnkCd = i['bnkCd']
            bnkImgUrl = i['bnkImgUrl']

            sql = "INSERT INTO _code_bank(bnkNm, bnkCd, bnkImgUrl) VALUES(%s, %s, %s)"
            val = (bnkNm, bnkCd, bnkImgUrl)
            print(type(val))

            curs.execute(sql, val)
            conn.commit()
    print(curs.rowcount, "record inserted")

if __name__ == '__main__':
    queryset()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/



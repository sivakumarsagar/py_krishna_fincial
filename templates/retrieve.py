def db_connect():
    # establsih the connection
    db_name = 'loan_data.db'
    db_con = sqlite3.connect(db_name)
    logging.info('Connected to '+db_name)
    return db_con
   cursor = db_connect()
query = "SELECT * FROM `loan_application`"
cursor.execute(query)
result = cursor.fetchall() 
final_result = [i[0] for i in result]
print(final_resul)

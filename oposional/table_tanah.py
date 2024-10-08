from koneksi import create_connection

def table_tanah():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('use dataset_lahan')

    sql_create_table = """ 
        create table if not exists tanah(
        id int not null auto_increment primary key,
        min_C1 float,
        max_C1 float,
        min_C2 float,
        max_C2 float,
        min_C3 float,
        max_C3 float,
        min_C4 float,
        max_C4 float,
        min_C5 float,
        max_C5 float,
        reading_time timestamp default current_timestamp              
    )
    """

    cursor.execute(sql_create_table)
    print ("Table tanah created successfully")
    cursor.close()
    connection.close()

if __name__ == "__main__":
    table_tanah()
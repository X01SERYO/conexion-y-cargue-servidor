import psycopg2
import getpass


def load(df, delete, insert):
    sms = ''
    try:
        # host 125.125.125.125
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()

        df['By'] = getpass.getuser()

        if delete:
            print('Realizando el delete')
            cursor.execute(delete)

        record_to_insert = df.values
        print('Realizando el insert')
        cursor.executemany(insert, record_to_insert)
        sms = str(cursor.rowcount) + " Registros cargadados exitosamente"
        connection.commit()
        cursor.close()
        connection.close()

    except Exception as e:
        print('end')
        connection.rollback()
        cursor.close()
        connection.close()
        print(e)
        sms = ('fail : ' + str(e))

    finally:
        print(sms)
        return sms

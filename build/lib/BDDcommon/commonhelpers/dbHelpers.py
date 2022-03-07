import pymysql
from BDDcommon.commonhelpers.credentialsHelper import CredentialsHelper

class DBHelpers(object):

    def __init__(self):
        cred_helper = CredentialsHelper()
        creds = cred_helper.get_db_credentials()
        self.host = 'localhost'
        self.db_user = creds['db_user']
        self.db_password = creds['db_password']

        #port or socket for local
        self.socket = 'socket Directory'

    def create_connection(self):

        self.connection = pymysql.connection(host=self.host, user=self.db_user,
                                             password=self.db_password, unix_socket=self.socket)

    def execute_select(self, sql):
        try:
            self.create_connection()
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise  Exception("Failed running sql {}. Error: {}".format(sql, str(e)))
        finally:
            self.connection.close()

        return rs_dict

    def execute_sql(self):
        pass

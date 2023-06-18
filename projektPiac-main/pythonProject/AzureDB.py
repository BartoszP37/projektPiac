import pypyodbc
import azurecred

class AzureDB:
    dsn='DRIVER='+azurecred.AZDBDRIVER+';SERVER='+azurecred.AZDBSERVER+';PORT=1433;DATABASE='+azurecred.AZDBNAME+';UID='+azurecred.AZDBUSER+';PWD='+ azurecred.AZDBPW

def __init__(self):
    self.conn = pypyodbc.connect(self.dsn)
    self.cursor = self.conn.cursor()
def finalize(self):
    if self.conn:
        self.conn.close()
def __exit__(self, exc_type, exc_val, exc_tb):
    self.finalize()
def __enter__(self):
    return self
def azureGetData(self):
    try:
        self.cursor.execute("SELECT nick,tekst,data_dodania from ksiega_gosci")
        data = self.cursor.fetchall()
        return data
    except pypyodbc.DatabaseError as exception:
        print('Failed to execute query')
        print(exception)
        exit (1)
def azureAddData(self):
    self.cursor.execute("INSERT into ksiega_gosci(nick, text, data_dodania) values (‘Marek’, ‘Podoba mi się’, GETDATE()),(‘Basia’, ‘Ciekawa stronka’, GETDATE())")
    self.conn.commit()

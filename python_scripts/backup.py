import os
from datetime import datetime

NOW = datetime.now()

BACKUP_DIR=os.environ.get('DB_BACKUP_DIR')
BACKUP_NAME=NOW.strftime("%Y%m%d_%H%M%S_PWDVault.sqlite")
DATABASE_DIR=os.environ.get('DATABASE_PATH')
DATABASE_NAME=os.environ.get('DATABASE_NAME')

os.system('sqlite3 {0}{1} ".backup {2}{3}"'.format(DATABASE_DIR, DATABASE_NAME, BACKUP_DIR, BACKUP_NAME))

print('backup script end')
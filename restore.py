import os
import sys
from datetime import datetime

NOW = datetime.now()

BACKUP_DIR=os.environ.get('DB_BACKUP_DIR')
BACKUP_NAME=NOW.strftime("%Y%m%d_%H%M%S_PWDVault.sqlite")
DATABASE_DIR=os.environ.get('DATABASE_PATH')
DATABASE_NAME=os.environ.get('DATABASE_NAME')
DATABASE_RESTORE_NAME=str(sys.argv[1])

os.system('sqlite3 {0} ".restore {1}{2}"'.format(DATABASE_NAME, DATABASE_DIR, DATABASE_RESTORE_NAME))

print('db restored')
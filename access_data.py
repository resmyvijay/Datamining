from azure.datalake.store import core,lib
import pandas as pd
from azure.datalake.store import core, lib, multithread

token = lib.auth(tenant_id='410552e4-1df2-4c98-86d4-09abad4c42e6', resource = 'https://datalake.azure.net/')

# Create an ADLS File System Client. The store_name is the name of your ADLS account
adlsFileSystemClient = core.AzureDLFileSystem(token, store_name='dmproject')

# Read a file into pandas dataframe
with adlsFileSystemClient.open('/mysampledirectory/flights21-Mar-2020_22-48.xlsx', 'rb') as f:
     df = pd.read_excel(f)
# Show the dataframe
print(df)
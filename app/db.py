from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.connection import register_connection,set_default_connection
import pathlib,config

settings = config.get_settings()
BASE_DIR = pathlib.Path(__file__).parent

def get_cluster():
    cloud_config= {
        'secure_connect_bundle': BASE_DIR / 'connect.zip'
    }
    auth_provider = PlainTextAuthProvider(
        settings.client_id,
        settings.client_secret
    )
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster
    
def get_session(): 
    cluster=get_cluster()
    session = cluster.connect()
    register_connection(str(session),session=session)
    set_default_connection(str(session))
    return session

if __name__ == 'main':
    session = get_session()
    row = session.execute("select release_version from system.local").one()
    if row:
        print(row[0])
    else:
        print("An error occurred.")

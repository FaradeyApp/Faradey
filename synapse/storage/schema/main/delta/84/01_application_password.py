import synapse.config.homeserver
import synapse.storage.engines
import synapse.storage.types


def run_create(
    cur: synapse.storage.types.Cursor,
    database_engine: synapse.storage.engines.BaseDatabaseEngine,
) -> None:
    if isinstance(database_engine, synapse.storage.engines.PostgresEngine):
        select_sql = """
            CREATE TABLE IF NOT EXISTS application_password (
                user_id TEXT NOT NULL,
                password TEXT NOT NULL
            );
        """
        cur.execute(select_sql)

def run_upgrade(
    cur: synapse.storage.types.Cursor,
    database_engine: synapse.storage.engines.BaseDatabaseEngine,
    config: synapse.config.homeserver.HomeServerConfig,
) -> None:
    if isinstance(database_engine, synapse.storage.engines.PostgresEngine):
        select_sql = """
            CREATE TABLE IF NOT EXISTS application_password (
                user_id TEXT NOT NULL,
                password TEXT NOT NULL
            );
        """
        cur.execute(select_sql)

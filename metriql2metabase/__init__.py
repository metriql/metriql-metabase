import argparse
import json
from .metadata import MetriqlMetadata
from .metabase import DatabaseOperation
import sys

__version__ = "0.3"


def main(args: list = None):
    parser = argparse.ArgumentParser(description="Synchronizes Metriql datasets to Metabase")

    parser.add_argument("command", choices=["create-database", "list-databases", "sync-database"],
                        help="command to execute")

    parser.add_argument("--metriql-url", help="metriql URL")
    parser.add_argument("--file", help="Read dataset from file instead of stdin")

    parser.add_argument("--database-id", help="Metabase database id that will be used to synchronize the datasets")
    parser.add_argument("--database-name", help="Metabase database name that will be used when creating databases")

    parser.add_argument("--metabase-url", help="Metabase URL that you want to analyze metriql data")

    parser.add_argument("--metabase-username", help="Metabase username for generating API token")
    parser.add_argument("--metabase-password", help="Metabase password for generating API token")

    parsed = parser.parse_args(args=args)
    operation = DatabaseOperation(parsed.metabase_url, parsed.metabase_username, parsed.metabase_password)
    if parsed.command == "create-database":
        operation.create_database(parsed.metriql_url, parsed.database_name)
        print('Successfully created!')
    if parsed.command == "list-databases":
        databases = operation.list_databases()
        print(json.dumps(databases))
    elif parsed.command == "sync-database":
        if parsed.file is not None:
            source = open(parsed.file).read()
        else:
            source = sys.stdin.readline()
        metriql_metadata = MetriqlMetadata(parsed.metriql_url, json.loads(source))
        if parsed.database_id is None:
            raise Exception("--database-id argument is required")
        operation.sync(int(parsed.database_id), metriql_metadata)

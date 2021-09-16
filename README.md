# Metriql Metabase Integration (WIP)

Synchronize Metabase datasets from Metriql datasets. The idea is to leverage Metriql datasets in your Metabase workflow without any additional modeling in Metabase.

### Usage

The library is available in PyPI so you can install it via pip as follows:

```
pip install metriql-metabase
```

The library expects `stdin` for the Metriql metadata and interacts with Metabase via its API. Here is an example:

```
curl http://metriql-server.com/api/v0/metadata | metriql-metabase --metriql-url http://metriql-server.com --metabase-username USERNAME --metabase-password PASSWORD sync-database
```

You can use `--file` argument instead of reading the metadata from `stdin` as an alternative.

Available commands are `create-database`, `list-databases`, `sync-database`.

### FAQ

#### Do you support Metabase Cloud?

Yes!


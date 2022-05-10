from snowflake.snowpark import Session
import snowflake.snowpark as snowpark
conn_param={
    "account": 'dhtnibu-sr17431',
    "user": 'edootechsnowflake',
    "password": 'Mynameis123',
    "database":"citibike",
    "warehouse":"compute_wh",
    "role":"sysadmin",
    "schema":"public"
}

session=Session.builder.configs(conn_param).create() 

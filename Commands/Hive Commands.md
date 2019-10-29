# Hive Commands


1. **Create Table:**  
```bash
	hive> create table <table_name> (<col1>, <col2>...);
```
2. **Load data:**
```bash
	hive> load data local <path> into table <table_name>;
```
3. **Drop Table:**
```bash
	hive> drop table <table_name>;
```
4. **Rename table:**
```bash
	hive> alter table <table_name> rename to <new_table_name>;
```
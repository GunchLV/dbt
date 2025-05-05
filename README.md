# DBT - DataBase Table reader
python class for super short DB table reading

✅ Basic Usage
* Classic way: just give the table name
> df = DBT("users")

* Even shorter: write table name as variable not string
> df = DBT(users)

🧠 Smart WHERE / SELECT / LIMIT Usage

* Select specific columns
> df = DBT("users", "name, age")

* WHERE clause (simple filtering)
> df = DBT("users", "age > 30")

* SELECT specific columns with WHERE clause
> df = DBT("users", "name, age", "age > 30")

* LIMIT rows with int
> df = DBT("users", 10)  # LIMIT 10

* WHERE + LIMIT with int
> df = DBT("users", "age > 30", 5)

* Full query with SELECT, WHERE, LIMIT
> df = DBT("users", "name, age", "age > 30", 5)

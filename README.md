# DB - DataBase Table reader
python class for super short DB table reading

✅ Basic Usage
* Classic way: just give the table name
> df = DB("users")

* Even shorter: write table name as variable not string
> df = DB(users)

🧠 Smart WHERE / SELECT / LIMIT Usage

* Select specific columns
> df = DB("users", "name, age")

* WHERE clause (simple filtering)
> df = DB("users", "age > 30")

* SELECT specific columns with WHERE clause
> df = DB("users", "name, age", "age > 30")

* LIMIT rows with int
> df = DB("users", 10)  # LIMIT 10

* WHERE + LIMIT with int
> df = DB("users", "age > 30", 5)

* Full query with SELECT, WHERE, LIMIT
> df = DB("users", "name, age", "age > 30", 5)

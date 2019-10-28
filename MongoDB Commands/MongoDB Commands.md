# MongoDB Important Commands

### Help Commands:
1. **List of all methods:**
```bash
	> db.help();
```
2. **Get stats of the db:**
```bash
	> db.stats();
```

### Collection:
1. **Create Collection:**
```bash
	> db.createCollection("collection_name");
```
2. **Show All Collection:**
```bash
	> show collections;
```

### Insert Commands:
1. **Simple Insert:**
```bash
	> db.student.insert({field: <value>});
```
- Here student is a collection. If the collection name already exists then it will append in the existing one, else it will create a new one, so no need to create collection in the first place.  
2. **Check if data inserted properly:**
```bash
	> db.student.find();
```
3. **Multiple Insert:**
```bash
	> db.student.insert([
		{	field: <value>
		},
		{	field: <value>
		}
	]);
```

### Update
1. **Update single parameters:**
```bash
	:'
	- first argument is check condition, here it will check the document for _id 1
	- second argument is the update statement, here roll_no will be updates to 5
	- thirs argument is optional. upsert means, if the document is not matched 
	  it will create a new one
	' 
	>db.student.update(
		{_id: "1"},
		{$set: {roll_no: 5}},
		{upsert: true}
	);
```
- Check [here](https://docs.mongodb.com/manual/reference/method/db.collection.update/) for more info on optional parameters.

2. **Update Multiple parameters:**
```bash
	> db.student.update(
		{_id: "1"},
		{$set: 
			{
				roll_no: 5,
				rank: 10
			}
		},
		{upsert: true}
	);
```
3. **Add a new attribute to the document:**
- It is same as above query , just remove the third argument.  
4. **Remove an attribute:**
- It is same as adding a new attribute, just change `$set` to `$unset`.  
5. **Save:**  
```bash
	> db.student.save();
```
6. **Update a specific document and include a new attribute for it:**  
```bash
	> db.food.update(
		{_id:4},
		{$push:{quantity:{orange:60,butterfruit:200,mango:120}}}
	);
```
7. **Update a specific document by adding elements to the array:**  
```bash
	> db.food.update({_id:3},{$addToSet:{fruits:"orange", "apple", "mango"}});
```
8. **Update a specific document by removing elements to the array:**  
```bash
	# 1 to remove last element and -1 to remove first
	> db.food.update({_id:4},{$pop:{fruits:1}});
```

### Searching
1. **Finding documents based on search criteria:**
```bash
	> db.student.find({name: "Bhushan"});
```
2. **Finding projection based on selection operators:**
```bash
	> db.student.find({_id: '1'},{studname: 1});
```
3. **Finding records with same matching criteria. (Equivalent to “=” clause**):
```bash
	> db.student.find({grade:{$eq:'VII'}});
```
4. **Finding records with not same matching criteria. (Equivalent to “!=” clause):**
```bash
	> db.student.find({grade: {$ne: 'VII'}});
```
5. **Finding records with greater than equal to criteria. (Equivalent to “>=” clause):**
```bash
	# for only greater than use $gt
	> db.student.find({roll: {$gte: 8}});
```
6. **Finding records with greater than equal to criteria. (Equivalent to “<=” clause):**  
```bash
	# for only less than use $lt
	> db.student.find({roll: {$lte: 8}});
```
7. **Finding records based on the AND Clause:**  
```bash
	> db.student.find({$and:[{school:'kv'},{ grade:'VII'}]});
```
8. **Finding records based on the AND Clause:**  
```bash
	> db.student.find({$or:[{school:'kv'},{ grade:'VII'}]});
```
9. **Finding records based on matching patterns:**  
```bash
	> db.student.find({studname:/^a/});
```
10. **Finding element with certain array positions:**  
```bash
	> db.food.find({'fruits.2':'grapes'});
```
11. **Finding documents having certain size of arrays:**  
```bash
	> db.food.find({'fruits':{$size:3}});
```

### Display
1. **Pretty print:**
```bash
	> db.student.find().pretty;
```
2. **Limit – this limits the display of output:**
```bash
	> db.students.find().limit(2);
```
3. **Skip – This skips the first n records:**
```bash
	> db.student.find().skip(2);
```
4. **Display selected array elements from a given document:**  
```bash
	> db.food.find({_id:1},{"fruits":{$slice:2}});
```
5. **Display all documents having the same array elements:**  
```bash
	> db.food.find({fruits:{$all:["banana","apple"]}});
```

### Delete
1. **Remove an element from the entire set of documents:**  
```bash
	> db.food.update({fruits:'mango'},{$pull:{fruits:'mango'}});
```

### JS Functions:
1. **Create a new function:**  
```bash
	> db.system.js.insert({
		_id: "factorial",
		value: function(n){
			if(n == 1)
				return 1;
			else
				return n*factorial(n-1);
		}
	});
```
2. **Executing the JS function:**  
```bash
	> db.eval("factorial(3)");
```

### Importing Files
1. **Import File:**  
```bash
	> mongoimport --db test --collection SampleJSON \
		--type csv --headerline --file words.csv
```
2. **Check whether the file has been imported or not:**  
```bash
	> db.SampleJSON.find().pretty();
```

### Map Reduce
1. **Creating a Map Function:**  
```bash
	> var map = function(){ 
 		emit(<key>, <value>);
 	};
```
2. **Creating a Reduce Function:**  
```bash
	> var reduce = function(key,values){
		return Array.sum(values);
	};
```
3. **Executing the Map Reduce Query:**
```bash
	> db.customer.mapReduce(map, reduce, {
		out:"Customer_totals", 
		query:{status:"A"}}
	);
```
# Pig Commands

1. **CopyFromLocal:**  
```bash
	grunt> copyFromLocal <path1> <path2> ;
```

2. **Dump:**  
```bash
	grunt> s = load '<path>' USING PigStorage(',') as \
			(param: <param_type>)
	grunt> dump s;
```

3. **Projections:**
```bash
	grunt> studentname = foreach <relation> generate <param>;
	grunt> dump studentname;
```

4. **Joins:**  

- Inner Join  
```bash
	grunt> JOIN <relation> by <col_name>, <relation> by <col_name>;
```
- Left Outer Join  
```bash
	grunt> JOIN <relation> by <col_name> LEFT OUTER, <relation> by <col_name>;
```
- Right Outer Join  
```bash
	grunt> JOIN <relation> by <col_name> RIGHT OUTER, <relation> by <col_name>;
```
- Full Outer Join  
```bash
	grunt> JOIN <relation> by <col_name> FULL OUTER, <relation> by <col_name>;
```

5. **Relational Operator:**  

- Cross  
```bash
	grunt> dump <relation1>;
	grunt> dump <relation2>;
	grunt> x = cross <relation1>, <relation2>;
	grunt> dump x;
```
- Distinct  
```bash
	grunt> z = distinct <relation>;  
	grunt> dump z;
```
- Filter  
```bash
	grunt> y = FILTER <relation> by <condition>;  
	grunt> dump y;
```
- ForEach  
```bash
	grunt> x = foreach <relation> generate <param1>, <param2>...<param_n>;  
	grunt> dump x;
```
- Cogroup  
```bash
	grunt> c = COGROUP <relation> by <param> inner, <relation> by <param> inner;  
	grunt> dump c; 
```
- Nested  
```bash
	grunt> c = COGROUP A by <param> inner, B by <param> inner;  
	grunt> dump c; 
	grunt> z = FOREACH C GENERATE group, B.b2;
	grunt> dump z;
	grunt> z = FOREACH C GENERATE group, A.(a1,a2);
	grunt> dump z;
```

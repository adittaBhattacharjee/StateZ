<h1 align="center">StateZ</h1>

<p>StateZ is simple programming language that is writted in Python 3.10. It does not have complex functionalities and is just made for fun. Stars are very much appreciated. Everyone can also contribute to the repository, just make a pull request.</p>

<h2 align="center">Usage</h2>

<h4>Create a new file called `hello_world.stz`. Then write:</h4>
 
 ```
 print('Hello, World!')
 ```

<h3>Running a file</h3>

Run from interpreter directly
```
python interpreter.py *your_filename.stz
```

Run from StateZ shell

```
python runtime_shell.py
$state> run("*your_filename.stz")
```

<h2 align='center'>Developers Guide</h2>
<h3 align='center'>General</h3>
`python runtime_shell.py` opens the StateZ shell. Running `run("*your_filename.stz")` from the shell executes code from your file.

<h3 align='center'>Variables</h3>

```
var cash = 100
var name = "Jake"
var new_cash = 100 + 10
var total_cash = cash + new_cash

print(cash)
print(name)
print(total_cash)
```
 Output:

 ```
 100
 Jake
 210
 ```

 <h3 align='center'>Conditions</h3>
 <h3 align='center'>if `condition` then `expression` elif `condtion` then `expression`<h3>

 ```
var cash = 100

if cash == 100 then var output=  "cash is 100" elif cash == 101 var output = "cash is "101" else var output("cash is something else")

print(output)
 ```

Output:

```
cash is 100
```

<h3 align='center'>Loops</h3>

```
for i = 0 to 3 then
    print("hello")
end
```

Output:

```
hello
hello
hello
```

<h3 align='center'>Functions</h3>

```
function call_great(prefix) -> prefix + " is great"
print(call_great("Aditya"))
```

Output

```
Aditya is great
```


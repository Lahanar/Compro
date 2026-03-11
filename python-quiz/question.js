const questions = [

{
question: "What is a common problem when developing large programs without functions?",
choices: [
"Programs run faster",
"Code becomes hard to read and maintain",
"Programs use less memory",
"No errors occur"
],
answer: "Code becomes hard to read and maintain"
},

{
question: "Why are functions useful in programming?",
choices: [
"They reduce code reuse",
"They make code reusable",
"They remove loops",
"They prevent syntax errors"
],
answer: "They make code reusable"
},

{
question: "What is a function in Python?",
choices: [
"A variable",
"A group of statements that perform a task",
"A loop",
"A data type"
],
answer: "A group of statements that perform a task"
},

{
question: "Which is a benefit of using functions?",
choices: [
"Code reuse",
"Better organization",
"Improved readability",
"All of the above"
],
answer: "All of the above"
},

{
question: "Which keyword defines a function in Python?",
choices: [
"function",
"def",
"func",
"define"
],
answer: "def"
},

{
question: "Which syntax correctly defines a function?",
choices: [
"function add(a,b)",
"def add(a,b):",
"define add(a,b)",
"func add(a,b)"
],
answer: "def add(a,b):"
},

{
question: "What symbol must appear after a function definition?",
choices: [
";",
":",
",",
"."
],
answer: ":"
},

{
question: "What is a parameter?",
choices: [
"Value passed into function",
"Return value",
"Loop variable",
"Global variable"
],
answer: "Value passed into function"
},

{
question: "How do you call a function?",
choices: [
"Write function name",
"Write function name with ()",
"Use call keyword",
"Use run keyword"
],
answer: "Write function name with ()"
},

{
question: "Given function greet(), how do you execute it?",
choices: [
"greet",
"greet()",
"call greet",
"run greet"
],
answer: "greet()"
},

{
question: "Functions can be called:",
choices: [
"Once only",
"Multiple times",
"Only inside loops",
"Only in classes"
],
answer: "Multiple times"
},

{
question: "What is the main advantage of calling functions?",
choices: [
"Reduce repeated code",
"Increase variables",
"Remove loops",
"Reduce libraries"
],
answer: "Reduce repeated code"
},

{
question: "A variable created inside a function is called:",
choices: [
"Global variable",
"Local variable",
"Public variable",
"External variable"
],
answer: "Local variable"
},

{
question: "Global variables can be accessed:",
choices: [
"Inside functions only",
"Anywhere in the program",
"Inside loops only",
"Inside classes only"
],
answer: "Anywhere in the program"
},

{
question: "Which keyword allows modifying global variables?",
choices: [
"global",
"static",
"external",
"public"
],
answer: "global"
},

{
question: "Local variables exist when:",
choices: [
"Program starts",
"Function is called",
"Loop starts",
"File opens"
],
answer: "Function is called"
},

{
question: "Which method adds items to a list?",
choices: [
"add()",
"append()",
"push()",
"insertItem()"
],
answer: "append()"
},

{
question: "range(5) produces:",
choices: [
"1-5",
"0-4",
"0-5",
"1-4"
],
answer: "0-4"
},

{
question: "What does a loop do?",
choices: [
"Repeat instructions",
"Delete lists",
"Create classes",
"Define functions"
],
answer: "Repeat instructions"
},

{
question: "What does this code create?\nfor i in range(5): nums.append(i)",
choices: [
"[0,1,2,3,4]",
"[1,2,3,4,5]",
"[0,1,2,3,4,5]",
"[]"
],
answer: "[0,1,2,3,4]"
},

{
question: "What is list comprehension?",
choices: [
"Short way to create lists",
"Sorting method",
"Delete method",
"Loop type"
],
answer: "Short way to create lists"
},

{
question: "Which is list comprehension syntax?",
choices: [
"[x for x in range(5)]",
"for x in range(5)",
"list(range(5))",
"range(5)"
],
answer: "[x for x in range(5)]"
},

{
question: "List comprehension makes code:",
choices: [
"Shorter",
"Cleaner",
"Readable",
"All of the above"
],
answer: "All of the above"
},

{
question: "Iteration part in list comprehension is:",
choices: [
"x",
"range(5)",
"for x in range(5)",
"[]"
],
answer: "for x in range(5)"
},

{
question: "What does [[0 for j in range(3)] for i in range(3)] create?",
choices: [
"3x3 matrix",
"1D list",
"Tuple",
"Dictionary"
],
answer: "3x3 matrix"
},

{
question: "Nested list comprehension creates:",
choices: [
"Dictionary",
"Matrix",
"Set",
"Tuple"
],
answer: "Matrix"
},

{
question: "Matrix is:",
choices: [
"1D array",
"2D array",
"String",
"Tuple"
],
answer: "2D array"
},

{
question: "List comprehension can also be used for:",
choices: [
"List",
"Set",
"Dictionary",
"All of the above"
],
answer: "All of the above"
},

{
question: "Matplotlib is used for:",
choices: [
"Web development",
"Data visualization",
"Database management",
"Networking"
],
answer: "Data visualization"
},

{
question: "Main plotting module in matplotlib is:",
choices: [
"plotlib",
"pyplot",
"draw",
"visual"
],
answer: "pyplot"
},

{
question: "Which command plots a graph?",
choices: [
"plt.plot()",
"plt.make()",
"plt.drawGraph()",
"plt.build()"
],
answer: "plt.plot()"
},

{
question: "Which command displays a graph?",
choices: [
"plt.open()",
"plt.show()",
"plt.display()",
"plt.run()"
],
answer: "plt.show()"
},

{
question: "NumPy is:",
choices: [
"Web library",
"Numerical computing library",
"GUI toolkit",
"Network tool"
],
answer: "Numerical computing library"
},

{
question: "NumPy is mainly used for:",
choices: [
"Arrays",
"Matrix operations",
"Math operations",
"All of the above"
],
answer: "All of the above"
},

{
question: "How do you create a NumPy array?",
choices: [
"np.make()",
"np.array()",
"np.create()",
"np.list()"
],
answer: "np.array()"
},

{
question: "How do you import NumPy?",
choices: [
"import numpy",
"import numpy as np",
"import np",
"import num"
],
answer: "import numpy as np"
},

{
question: "What does a + b do for numpy arrays?",
choices: [
"Concatenate arrays",
"Element-wise addition",
"Matrix multiply",
"Error"
],
answer: "Element-wise addition"
},

{
question: "np.mean(a) returns:",
choices: [
"Maximum",
"Minimum",
"Average",
"Sum"
],
answer: "Average"
},

{
question: "a[0] returns:",
choices: [
"First element",
"Last element",
"Entire array",
"Slice"
],
answer: "First element"
},

{
question: "a[1:3] is:",
choices: [
"Slicing",
"Sorting",
"Append",
"Delete"
],
answer: "Slicing"
},

{
question: "np.dot(a,b) performs:",
choices: [
"Addition",
"Matrix multiplication",
"Division",
"Subtraction"
],
answer: "Matrix multiplication"
},

{
question: "Matrix operations are common in:",
choices: [
"Linear algebra",
"Graphics",
"Machine learning",
"All of the above"
],
answer: "All of the above"
},

{
question: "Which library works well with NumPy for plotting?",
choices: [
"Flask",
"Matplotlib",
"Django",
"Tkinter"
],
answer: "Matplotlib"
},

{
question: "NumPy arrays are faster than Python lists because:",
choices: [
"They use optimized C code",
"They use less RAM always",
"They remove loops",
"They avoid functions"
],
answer: "They use optimized C code"
}

];

const quiz = [

{
question: "What keyword is used to define a function in Python?",
choices: ["function", "def", "func", "define"],
answer: 1
},

{
question: "What does this code return? def add(a,b): return a+b",
choices: ["sum of a and b", "product", "string", "error"],
answer: 0
},

{
question: "Which syntax is List Comprehension?",
choices: [
"[i for i in range(5)]",
"for i in range(5)",
"list(range(5))",
"range(5)"
],
answer: 0
},

{
question: "Which module is commonly used for plotting graphs?",
choices: [
"numpy",
"pyplot",
"pandas",
"sklearn"
],
answer: 1
},

{
question: "Which library is used for numerical arrays in Python?",
choices: [
"numpy",
"matplotlib",
"flask",
"django"
],
answer: 0
}

]

let currentQuestion = 0
let score = 0

function loadQuestion(){

let q = quiz[currentQuestion]

document.getElementById("question").innerText =
"Question " + (currentQuestion+1) + ": " + q.question

let choicesHTML = ""

for(let i=0;i<q.choices.length;i++){

choicesHTML +=
`<input type="radio" name="choice" value="${i}">
${q.choices[i]}<br>`

}

document.getElementById("choices").innerHTML = choicesHTML

document.getElementById("result").innerText = ""

}

function checkAnswer(){

let choices = document.getElementsByName("choice")

let selected = -1

for(let i=0;i<choices.length;i++){
if(choices[i].checked){
selected = choices[i].value
}
}

if(selected == -1){
alert("Please select an answer")
return
}

let correct = quiz[currentQuestion].answer

if(selected == correct){

document.getElementById("result").innerText = "Correct!"
score++

}else{

document.getElementById("result").innerText =
"Wrong! Correct answer is: " +
quiz[currentQuestion].choices[correct]

}

}

function nextQuestion(){

currentQuestion++

if(currentQuestion < quiz.length){

loadQuestion()

}else{

document.getElementById("question").innerText = "Quiz Completed"

document.getElementById("choices").innerHTML = ""

}

}

function showScore(){

document.getElementById("score").innerText =
"Your Score: " + score + " / " + quiz.length

}

loadQuestion()

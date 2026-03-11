let currentQuestion = 0;
let score = 0;

function loadQuestion(){

let q = questions[currentQuestion];

document.getElementById("question").innerText = q.question;

let choicesHTML="";

q.choices.forEach(choice=>{
choicesHTML += `
<label>
<input type="radio" name="choice" value="${choice}">
${choice}
</label><br>
`;
});

document.getElementById("choices").innerHTML = choicesHTML;
}

function checkAnswer(){

let selected = document.querySelector('input[name="choice"]:checked');

if(!selected) return;

if(selected.value === questions[currentQuestion].answer){

document.getElementById("result").innerText = "Correct!";
score++;

}else{

document.getElementById("result").innerText = "Wrong!";
}

}

function nextQuestion(){

currentQuestion++;

if(currentQuestion < questions.length){

loadQuestion();
document.getElementById("result").innerText="";

}else{

document.getElementById("question").innerText="Quiz Finished!";
document.getElementById("choices").innerHTML="";
}

}

function showScore(){

document.getElementById("score").innerText =
"Your Score: " + score + " / " + questions.length;

}

loadQuestion();

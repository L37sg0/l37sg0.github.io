/*Rules:
 The player throws a pair of dice, with max of 3 throws.
The sum of the two top faces is what matters so a 1 and 3
is the same as 2 and 2. The sum of two 6 sided dice can be
any number from 2 to 12. If the player throws a 7 or 11
on the first throw, the player wins. If the player throws
a 2, 3, or 12, the player loses. For any other result
(4, 5, 6, 8, 9, 10), this result is recorded as what
is called the player's point and a follow-up throw is
required. On follow-up throws, a throw of 7 loses and a
throw of the player's point wins. For anything else, the
game continues with the follow-up throw rules.
*/

var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

// Define the Throw button:
var but = document.getElementById("button");
var buton = but.getContext("2d");


buton.fillStyle = "white";
buton.font = "20px Verdana";
buton.fillText("Throw!", 5, 30);

but.addEventListener("click", function(){
	roll();
	Buton();
});

function Buton() {
	but.style.background = "linear-gradient(grey, black)";
	setTimeout(function(){ 
			but.style.background = "linear-gradient(black, grey)";
		}, 100);
}

// Define Dices:
var dieOne = 6;
var dieTwo = 6;
var diceRoll = new Audio();// Plays a rolling dices sound.
diceRoll.src = "http://cd.textfiles.com/itcontinues/WIN/YTB22/MANYDICE.WAV";

var result = 0;
var prev = 0;
var turns = 3;
var msg = "Press Throw to play."
var firstRoll = null;

function roll() {// Get random number from 1 to 6, when called.
	diceRoll.play();
	dieOne = Math.floor(Math.random()*6) + 1;
	dieTwo = Math.floor(Math.random()*6) + 1;
	if (msg == "You Win!" || msg == "You Lose!") {
		location.reload();
	}
	if (firstRoll == null){firstRoll=true;}
	//Detect the rules:
	if (firstRoll) {
		firtsRules();
	}else{if(firstRoll == false)
		{secondRules();}
	}
}

function firtsRules(){
	result = dieOne + dieTwo;
	switch(result) {
		case 2:
		case 3:
		case 12:
			msg = "You Lose!";
			break;
		case 7:
		case 11:
			msg = "You Win!";
			break;
		default:
			firstRoll=false;
			turns -= 1;
			break;
	}
}

function secondRules(){
	prev = result;
	result = dieOne + dieTwo;
	turns -= 1;
	if(turns <= 0 || result == 7) {
		msg = "You Lose!";
		
	}
	if(result == prev) {
		msg = "You Win!";
	}

}


// Drawing the dots in the dice.
function drawOne(between){//One middle dot.
	ctx.beginPath();
	ctx.arc(60+between,60, 5,0, Math.PI*2, true);
	ctx.fill();
	ctx.closePath();		
}

function drawTwo(between){// Two oposite dots.
	ctx.beginPath();
	ctx.arc(30+between,30, 5,0, Math.PI*2, true);
	ctx.fill();
	ctx.closePath();		
	ctx.beginPath();
	ctx.arc(90+between,90, 5,0, Math.PI*2, true);
	ctx.fill();
	ctx.closePath();		
}

function drawFour(between) {// Four dots.
	drawTwo(between);
	ctx.beginPath();
	ctx.arc(30+between,90, 5,0, Math.PI*2, true);
	ctx.fill();
	ctx.closePath();		
	ctx.beginPath();
	ctx.arc(90+between,30, 5,0, Math.PI*2, true);
	ctx.fill();
	ctx.closePath();
}

function drawMid(between) {// Two dots in the mid, for number 6 called.
	ctx.beginPath();
	ctx.arc(30+between,60, 5,0, Math.PI*2, true);
	ctx.fill();
	ctx.closePath();		
	ctx.beginPath();
	ctx.arc(90+between,60, 5,0, Math.PI*2, true);
	ctx.fill();
	ctx.closePath();
}
//Drawing the dice
function drawDice(diceX, diceY, scale, between, die, sideColor, dotColor){
	ctx.fillStyle = sideColor;// Color of the dice side.
	ctx.fillRect(diceX, diceY, scale, scale);
	ctx.fillStyle = dotColor;// Color of the dice dots.
	switch(die) {// Dice conditions for drawing dots.
		case 1:{drawOne(between); break;}
		case 2:{drawTwo(between); break;}
		case 3:{
			drawOne(between);
			drawTwo(between);
			break;
		}
		case 4:{
			drawFour(between);
			break;
		}
		case 5:{
			drawOne(between);
			drawFour(between);
			break;
		}
		case 6:{
			drawMid(between);
			drawFour(between);
			break;
		}
		default: break;
	}
}

// The final drawing of the game.


function draw(){
	ctx.clearRect(0,0,500,380);
	
	// Make some gradient colors for the dices:
	var my_black = ctx.createLinearGradient(0,0,0,170);
	my_black.addColorStop(0,"black");
	my_black.addColorStop(1,"grey");
	
	var my_white = ctx.createLinearGradient(0,0,0,170);
	my_white.addColorStop(0,"white");
	my_white.addColorStop(1,"black");
	
	drawDice(10, 10, 100, 0, dieOne, my_black, "white");
	drawDice(120, 10, 100, 110, dieTwo, my_white, "black");
	
	//Define the msg box:
	ctx.fillStyle = "black";
	ctx.font = "30px Verdana";
	ctx.fillText("Result: "+result, 10, cvs.height/2);
	ctx.fillText("Previous: "+prev, 200, cvs.height/2);
	ctx.fillText(msg, 10, (cvs.height/2)+40);
	ctx.fillText("Remaining: "+turns, 10, (cvs.height/2)+80);

	
	requestAnimationFrame(draw);
}
draw();

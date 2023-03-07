// Getting input via STDIN
const readline = require("readline");

const inp = readline.createInterface({
  input: process.stdin
});

const userInput = [];

inp.on("line", (data) => {
  userInput.push(data);
});

inp.on("close", () => {
  //start-here
  //Your code goes here … replace the below line with your code logic
    
    let [number1, number2] = userInput[0].split(' ').map((item) => parseInt(item));

    let factor = number1 < number2 ? number1 : number2;

    if (number1 % factor == 0 && number2 % factor == 0) {
        console.log(factor);
    } else {
        factor--;
        while (factor>0) {
            if (number1 % factor == 0 && number2 % factor == 0) {
                console.log(factor);
                break;
            } else {
                factor--;
            }
        }
    }



  //end-here
});
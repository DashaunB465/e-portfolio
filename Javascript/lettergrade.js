"use strict"

// assume all user inputs are valid
const firstname = prompt("Enter Studnet first: ", "Jane Doe");
const grade1 = parseInt(prompt("Enter first grade score (1-100):",100));
const grade2 = parseInt(prompt("Enter second grade score (1-100):",75));
const grade3 = parseInt(prompt("Enter third grade score (1-100):",50));

let highest1 = 0;
let highest2 = 0;


// Funtion 1
// calculate the average of 2 highest grades
function average(score1, score2, score3){
    if (score1 < score2){
        highest1 = score2;
    }else if(score1 < score3){
        highest2 = score3;
    } else {
        highest1 = score1;
        highest2 = score2;
    }
    let avg = (highest1 + highest2) / 2;
    // or do this
    // let avg = (score1 + score2 + score3 - Math.min(score1, score2, score3))/ 2;
    return avg;

    
}

// Funtion 2
// convert average to letter grade
function avgToLetter(avg){
    if(avg >= 90){
        return "A";
    }else if(avg > 79.9 && avg < 90){
        return "B";
    }else if(avg > 69.9 && avg <= 79.9){
        return "C";
    }else if(avg > 59.9 && avg <= 69.9){
        return "D";
    }else{
        return "F";
    }
}

// Function 3
// Display info
const displayInfo = (name, grade) => {
    document.write(name + " earned a " + grade +"<br>");
}

// call funtions
const av = average(grade1, grade2, grade3);
const letterGrade = avgToLetter(av);
displayInfo(firstname, letterGrade);
"use strict";

const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let sales = [0, 0, 0, 0, 0, 0, 0];

$(() => {
    $("#update").click(() => {
        const w = $("#sales").val();
        const a = parseFloat($("#amount").val());
        if (w == "x") {
            alert("Choose a weekday");
        }
        else if (isNaN(a) || a < 0) {
            alert("Sales amount must be positive number")
        } else {
            sales[w] = a;
            display();
        }
    });
    $("#clear").click(() => {
        sales = [0, 0, 0, 0, 0, 0, 0];
        $("#sales").val("x");
        $("#amount").val("");
        display();
    });
    const display = () => {
        let result = "<label>Weekday</label><label>Amount</label><hr>";
        let sum = 0;
        for (let w = 0; w < 7; w++) {
            result += "<label>" + weekdays[w] + "</label>";
            result += "<label>$" + sales[w].toFixed(2) + "</label><br>";
            sum += sales[w];
        }
        result += "<hr><label>Total Sales:</label>";
        result += "<label>$" + sum.toFixed(2) + "</label>";
        $("#output").html(result);
    };
    display();
});

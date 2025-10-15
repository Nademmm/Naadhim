function appendValue(value) {
    const display = document.getElementById("display");
    display.value += value;
}

function clearDisplay() {
    document.getElementById("display").value = "";
}

function calculate() {
    const display = document.getElementById("display");
    let ekspresi = display.value;

    try {
        ekspresi = ekspresi.replace(/%/g, "/100");

        ekspresi = ekspresi.replace(/\^2/g, "**2");

        display.value = eval(ekspresi);
    } catch {
        display.value = "Error";
    }
}

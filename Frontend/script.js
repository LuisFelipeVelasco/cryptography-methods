let selectedMethod = "";
let selectedAction = "";
let loadingInterval;

// METHOD SELECTION
document.querySelectorAll("input[name='method']").forEach(radio => {
    radio.addEventListener("change", () => {
        selectedMethod = radio.value;
        updateKeyVisibility();
    });
});

// ACTION BUTTONS
document.querySelectorAll(".actions button").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".actions button")
            .forEach(b => b.classList.remove("active"));

        btn.classList.add("active");
        selectedAction = btn.dataset.action;
        updateKeyVisibility();
    });
});

// KEY VISIBILITY LOGIC
function updateKeyVisibility() {
    const keyBox = document.getElementById("keyBox");

    if (
        (selectedMethod === "caesar" || selectedMethod === "transposition") &&
        selectedAction !== "break"
    ) {
        keyBox.style.display = "block";
    } else {
        keyBox.style.display = "none";
    }
}

// LOADING ANIMATION
function startLoading() {
    const loading = document.getElementById("loading");
    loading.style.display = "block";
    let dots = 0;

    loadingInterval = setInterval(() => {
        dots = (dots + 1) % 4;
        loading.textContent = "loading" + ".".repeat(dots);
    }, 500);
}

function stopLoading() {
    clearInterval(loadingInterval);
    document.getElementById("loading").style.display = "none";
}

// SUBMIT
document.getElementById("submitBtn").addEventListener("click", () => {
    const output = document.getElementById("outputBox");
    output.textContent = "";

    startLoading();

    setTimeout(() => {
        stopLoading();
        output.textContent =
            "Result appears here.\n\n" +
            "Method: " + selectedMethod + "\n" +
            "Action: " + selectedAction;
    }, 2500);
});

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
        (selectedMethod === "cesar" || selectedMethod === "transposition") &&
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
document.getElementById("submitBtn").addEventListener("click", async () => {
    startLoading()
    updateOutputText(" ")
    const result = await callApis();
    updateOutputText(result);
    stopLoading()
});

// CAll THE ENCRYPTION METHOD

async function callApis() {
    key = parseInt(document.getElementById("keySelect").value, 10);
    message = document.getElementById("inputText").value;
    Url = getUrl();
    Output = await fetch(Url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            key: key,
            message: message
        })
    });
    finalOutput = await Output.json();
    return finalOutput.result;
}

//UPDATE THE BOX WHERE THE ANSWER IS SHOWED

function updateOutputText(message) {
    text = document.getElementById("outputBox");
    text.textContent = message;

}

//CREATE A URL DEPENDING OF THE CRIPTOGRAPHY METHOD

function getUrl() {
    if (selectedMethod == "atbash") {
        Url = `https://cryptography-methods.up.railway.app/atbash`
    }
    else {
        Url = `https://cryptography-methods.up.railway.app/${selectedMethod}/${selectedAction}`;
    }
    return Url
}
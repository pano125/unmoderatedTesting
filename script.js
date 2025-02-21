document.getElementById("testForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let task = document.getElementById("task").value;
    let figmaUrl = document.getElementById("figmaUrl").value;
    let testId = "test_" + Date.now();  // Генерируем уникальный ID

    fetch("publish.py", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ testId, task, figmaUrl })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = 
            `<p>Тест создан! <a href="tests/${testId}.html" target="_blank">Перейти</a></p>`;
    });
});
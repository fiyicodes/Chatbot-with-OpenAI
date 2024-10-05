function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    // Display user message
    const userMessage = `<div class="mb-2 text-end"><strong>You:</strong> ${userInput}</div>`;
    chatBox.innerHTML += userMessage;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send request to Flask backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display AI response
        const aiMessage = `<div class="mb-2 text-start"><strong>AI:</strong> ${data.message}</div>`;
        chatBox.innerHTML += aiMessage;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Clear input field
    document.getElementById("user-input").value = '';
}

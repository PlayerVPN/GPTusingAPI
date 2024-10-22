function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Append user message to chat box
    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("p");
    userMessage.textContent = `You: ${userInput}`;
    chatBox.appendChild(userMessage);

    // Send message to the backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement("p");
        botMessage.textContent = `Bot: ${data.response}`;
        chatBox.appendChild(botMessage);

        // Clear the input field
        document.getElementById("user-input").value = '';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

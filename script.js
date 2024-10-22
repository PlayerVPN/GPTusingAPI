function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Append user message to chat box
    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = `You: ${userInput}`;
    chatBox.appendChild(userMessage);
    chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll

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
        const botMessage = document.createElement("div");
        botMessage.className = "bot-message";
        botMessage.textContent = `Bot: ${data.response}`;
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll

        // Clear the input field
        document.getElementById("user-input").value = '';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

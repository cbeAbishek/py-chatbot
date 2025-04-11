const chatbox = document.getElementById('chatbox');

function addMessage(text, sender) {
  const msg = document.createElement('div');
  msg.className = 'msg ' + sender;
  msg.textContent = sender === 'user' ? "You: " + text : "Bot: " + text;
  chatbox.appendChild(msg);
  chatbox.scrollTop = chatbox.scrollHeight;
}

async function sendQuestion() {
  const input = document.getElementById('userInput');
  const question = input.value.trim();
  if (!question) return;

  addMessage(question, 'user');
  input.value = '';

  const response = await fetch('https://py-chatbot-2kx8.onrender.com/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question: question })
  });

  const data = await response.json();
  addMessage(data.answer, 'bot');

  if (data.answer.includes("Can you teach me?")) {
    const teachAnswer = prompt("Please provide the correct answer:");
    if (teachAnswer) {
      await fetch('https://py-chatbot-2kx8.onrender.com/teach', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: question, answer: teachAnswer })
      });
      addMessage("Thanks! I've learned a new answer.", 'bot');
    }
  }
}

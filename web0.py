from flask import Flask, request, jsonify
import test

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <form action="/chat" method="post">
        <input type="text" name="message" placeholder="Type your message here">
        <button type="submit">Send</button>
    </form>
    <div id="chat-box"></div>
    <script>
        function sendMessage() {
            var message = document.querySelector('input[name="message"]').value;
            var chatBox = document.getElementById('chat-box');
            var userMessage = document.createElement('p');
            userMessage.textContent = "You: " + message;
            chatBox.appendChild(userMessage);

            // Send message to server
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                var serverMessage = document.createElement('p');
                serverMessage.textContent = "Server: " + data.reply;
                chatBox.appendChild(serverMessage);
                document.querySelector('input[name="message"]').value = '';
            });

            return false;
        }

        document.querySelector('form').onsubmit = sendMessage;
    </script>
    """

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    reply = test.main(message)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run()

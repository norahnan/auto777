from flask import Flask, request, jsonify
import test

app = Flask(__name__)

@app.route('/')
def index():
    return """
    
    
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>美化的简易聊天框</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        #chat-container {
            width: 75%; /* 将宽度改为百分比 */
            max-width: 800px; /* 设置最大宽度，避免在大屏幕上拉伸过度 */
            margin: 50px auto;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        #chat-messages {
            height: 370px;
            overflow-y: scroll;
            border-bottom: 1px solid #ccc;
            padding: 10px;
            display: flex;
            flex-direction: column;
        }
        #message-input {
            width: calc(100% - 70px);
            border: none;
            padding: 10px;
            font-size: 16px;
            outline: none;
        }
        #message-input:focus {
            border-bottom: 2px solid #007bff;
        }
        #send-button {
            width: 70px;
            border: none;
            background-color: #007bff;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        #send-button:hover {
            background-color: #0056b3;
        }
        .message {
            background-color: #f0f0f0;
            border-radius: 5px;
            padding: 8px 12px;
            margin: 5px 0;
            font-size: 14px;
            align-self: flex-start; /* 让系统回复消息靠左显示 */
        }
        .user-message {
            background-color: #e2e2ff;
            align-self: flex-end; /* 让用户消息靠右显示 */
        }
    </style>
    </head>
    <body>



<form action="/chat" method="post">
        <div id="chat-container">
    <div id="chat-messages"></div>
    <div style="display: flex; align-items: center; padding: 5px;">
        <input type="text" id="message-input" name="message" placeholder="输入消息">
        <button id="send-button">发送</button>
    </div>
</div>
    </form>
   
    
    
    
    <script>
    
   
        function sendMessage() {
    var messageInput = document.getElementById("message-input");
    var message = messageInput.value.trim();
    if (message === "") {
        return;
    }
    var chatMessages = document.getElementById("chat-messages");

    // 用户发送的消息
    var userMessage = document.createElement("div");
    userMessage.textContent = message;
    userMessage.classList.add("message", "user-message");
    chatMessages.appendChild(userMessage);

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
    
    
        
        
        var serverMessage = document.createElement("div");
        serverMessage.textContent = data.reply;
        serverMessage.classList.add("message");
        chatMessages.appendChild(serverMessage);
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

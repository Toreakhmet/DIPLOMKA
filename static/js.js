document.addEventListener("DOMContentLoaded", function() {
  
    // Получаем все карточки товара
    const productCards = document.querySelectorAll('.product-card');
    
    productCards.forEach((card) => {
      
      // Добавляем анимацию "подпрыгивания" при наведении
      card.addEventListener('mouseenter', function() {
        card.style.transform = 'scale(1.05)';
      });
  
      // Убираем анимацию при убирании мыши
      card.addEventListener('mouseleave', function() {
        card.style.transform = 'scale(1)';
      });
      
    });
  
  });

  document.addEventListener('DOMContentLoaded', function() {
    const chatInput = document.getElementById("chat-input");
    const chatSend = document.getElementById("chat-send");
    const chatBody = document.getElementById("chat-body");

    chatSend.addEventListener('click', function() {
        const message = chatInput.value;

        if (message) {
            // Отправить сообщение на сервер (это просто пример, на практике используйте AJAX или WebSockets)
            // ...

            // Добавить сообщение в чат
            const messageDiv = document.createElement('div');
            messageDiv.className = 'user-message';
            messageDiv.innerText = message;
            chatBody.appendChild(messageDiv);

            // Очистить поле ввода
            chatInput.value = '';
        }
    });
});

  
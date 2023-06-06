const searchInput = document.getElementById('search-input');

searchInput.addEventListener('input', function() {
  const query = searchInput.value.trim();

  // Отправка запроса на сервер Django при изменении значения в поле поиска
  fetch(`/search/?query=${query}`)
    .then(response => response.json())
    .then(data => {
      // Обновление списка товаров на основе полученных данных
      updateProducts(data);
      addEventListeners();
    })
    .catch(error => {
      console.error('Ошибка при выполнении запроса поиска:', error);
    });
});

function updateProducts(productsData) {
  var productsContainer = document.querySelector('.products-container');
  productsContainer.innerHTML = ''; // Очистка контейнера товаров перед обновлением

  productsData.products.forEach(function(product) {
    var productElement = document.createElement('div');
    productElement.classList.add('product');

    var productContent = document.createElement('div');
    productContent.classList.add('product-content');

    var productName = document.createElement('h3');
    productName.textContent = product.name;

    var productQuantity = document.createElement('p');
    productQuantity.textContent = 'Кол-во: ' + product.quantity + ' ' + product.unit;

    var lastUpdated = document.createElement('p');
    lastUpdated.classList.add('last-updated');
    lastUpdated.textContent = 'Последнее обновление: ' + product.last_updated;

    var productControls = document.createElement('div');
    productControls.classList.add('product-controls');

    var quantityInput = document.createElement('input');
    quantityInput.setAttribute('type', 'number');
    quantityInput.setAttribute('min', '1');
    quantityInput.setAttribute('value', '1');

    var addButton = document.createElement('button');
    addButton.classList.add('add-button');
    addButton.textContent = '+';
    addButton.setAttribute('data-product-id', product.id);

    var deleteButton = document.createElement('button');
    deleteButton.classList.add('delete-button');
    deleteButton.textContent = 'Удалить';
    deleteButton.setAttribute('data-product-id', product.id);

    productControls.appendChild(quantityInput);
    productControls.appendChild(addButton);
    productControls.appendChild(deleteButton);

    productContent.appendChild(productName);
    productContent.appendChild(productQuantity);
    productContent.appendChild(lastUpdated);
    productContent.appendChild(productControls);

    productElement.appendChild(productContent);
    productsContainer.appendChild(productElement);
  });
  addEventListeners();
}



function addEventListeners() {
  const deleteButtons = document.querySelectorAll('.delete-button');
  const addButton = document.querySelectorAll('.add-button');
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  deleteButtons.forEach(button => {
    button.addEventListener('click', function() {
      const productId = this.getAttribute('data-product-id');

      // Отправка запроса на удаление товара с CSRF-токеном
      fetch(`/delete-product/${productId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
          'Content-Type': 'application/json'
        }
      })
        .then(response => response.json())
        .then(data => {
          // Обработка успешного удаления товара
          console.log(data.message);
          // Удаление элемента товара из DOM
          const productElement = this.closest('.product');
          productElement.remove();
        })
        .catch(error => {
          // Обработка ошибки удаления товара
          console.error('Ошибка при выполнении запроса на удаление товара:', error);
        });
    });
  });

  addButton.forEach(button => {
    button.addEventListener('click', function() {
      const productElement = this.closest('.product');
      const productId = this.getAttribute('data-product-id');
      const quantityInput = productElement.querySelector('input[type=number]');
      const quantity = quantityInput.value;

      // Создаем экземпляр FormData и добавляем данные формы
      const formData = new FormData();
      formData.append('quantity', quantity);

      // Отправка запроса на добавление количества товара с CSRF-токеном
      fetch(`/add-quantity/${productId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken
        },
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          // Обработка успешного добавления количества товара
          console.log(data.message);
          // Обновление значения количества товара в DOM
          const quantityElement = productElement.querySelector('.quantity');
          quantityElement.textContent = `Кол-во: ${data.quantity} ${data.unit}`;
        })
        .catch(error => {
          // Обработка ошибки добавления количества товара
          console.error('Ошибка при выполнении запроса на добавление количества товара:', error);
        });
    });
  });
}

addEventListeners();
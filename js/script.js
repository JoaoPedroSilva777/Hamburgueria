// script.js

// Espera o carregamento completo da página
document.addEventListener("DOMContentLoaded", function () {
  // Seleciona o botão "Ver Cardápio"
  const botaoCardapio = document.querySelector(".botao");

  if (botaoCardapio) {
    botaoCardapio.addEventListener("click", function (e) {
      // Pode mostrar um alerta divertido
      alert("Preparando o cardápio para você! 🍔");
    });
  }

  // Exemplo: Se você adicionar um formulário de contato, pode validar assim:
  const formContato = document.querySelector("#form-contato");
  if (formContato) {
    formContato.addEventListener("submit", function (e) {
      const nome = formContato.querySelector('input[name="nome"]').value.trim();
      const email = formContato.querySelector('input[name="email"]').value.trim();

      if (!nome || !email) {
        e.preventDefault();
        alert("Por favor, preencha nome e email antes de enviar!");
      }
    });
  }
});

// Pega o botão pelo ID
let mybutton = document.getElementById("btn-back-to-top");

// Quando o usuário rolar 20px para baixo, mostra o botão
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// Quando clicar no botão, rola para o topo suavemente
mybutton.addEventListener("click", backToTop);

function backToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}